# TorquePlotter.py
# Quick and dirty GUI for reading incoming serial port data from the Torque Meter
# plotting the data and saving it as csv file
import datetime
import io
import logging
import typing
import numpy as np
import serial
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QComboBox,
    QPlainTextEdit,
    QStatusBar,
    QFileDialog,
    QGroupBox,
    QMessageBox,
    QMainWindow,
    QApplication, QAction,
)
import pyqtgraph as pg
import pyqtgraph.exporters
from pathlib import Path
from serial.tools import list_ports
import argparse

UPDATE_PERIOD = 100  # in ms
DATE_FORMAT = "%Y%m%d"  # format of the date added to the filename

parser = argparse.ArgumentParser()
parser.add_argument(
    "--log-level",
    help="level of information to log. "
    "Can be one of [DEBUG,INFO,WARNING,ERROR,CRITICAL]. "
    "Default is WARNING",
    default="WARNING",
)
parser.add_argument(
    "--log-file",
    help="file in which the log is written. "
    "If absent or None, log is directed to stdout",
    default=None,
)
args = parser.parse_args()

# see https://docs.python.org/3/howto/logging.html#logging-to-a-file
numeric_level = getattr(logging, args.log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError(f"Invalid log level: {args.log_level}")
logger = logging.getLogger(__name__)
logging.basicConfig(level=numeric_level, filename=args.log_file, filemode="w")
script_root = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    infoGroupBox: QGroupBox
    serialGroupBox: QGroupBox
    startButton: QPushButton
    stopButton: QPushButton
    serialConnectButton: QPushButton
    rootPathEdit: QLineEdit
    refreshSerialButton: QPushButton
    browseButton: QPushButton
    baudRateComboBox: QComboBox
    subjectIDEdit: QLineEdit
    serialOutputWidget: QPlainTextEdit
    serialPortsComboBox: QComboBox
    plotView: pg.PlotWidget
    # noinspection SpellCheckingInspection
    statusbar: QStatusBar
    action_Quit: QAction
    action_Open: QAction
    serial: typing.Union[None, serial.Serial]

    def __init__(self) -> None:
        # noinspection PyArgumentList
        super(MainWindow, self).__init__()
        uic.loadUi(script_root.joinpath("MainWindow.ui"), self)  # Load the .ui file

        self.subjectIDMissingStylesheet = "background:red"

        self.basename = ""
        self.serial = None
        self.sio = None
        self.file = None
        self.serial_ports = []
        self.list_serial_ports()

        self.rootPath = Path.cwd()
        self.rootPathEdit.setText(self.rootPath.as_posix())

        self.refreshSerialButton.clicked.connect(self.list_serial_ports)
        self.browseButton.clicked.connect(self.browse_root_path)
        self.serialConnectButton.clicked.connect(self.connect_serial)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.action_Open.triggered.connect(self.action_open_file)
        self.action_Quit.triggered.connect(self.close)
        self.subjectIDEdit.textEdited.connect(self.subject_id_edited)

        self.plotItem: pg.PlotItem = self.plotView.getPlotItem()
        self.plotItem.setLabels(left="Force (gf)", bottom="Angle (deg)")
        self.plotItem.showGrid(x=True, y=True, alpha=0.5)
        self.curve = self.plotItem.plot(symbol="o")
        self.data = np.ndarray(shape=(0, 2))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.stop()

        self.show()  # Show the GUI

    def connect_serial(self):
        if self.serialConnectButton.isChecked():
            # button is checked, connecting...
            logger.debug(
                f"Attempting to connect to {self.serialPortsComboBox.currentData().device}, "
                f"baudrate={int(self.baudRateComboBox.currentText())}"
            )
            try:
                self.serial = serial.Serial(
                    port=self.serialPortsComboBox.currentData().device,
                    baudrate=int(self.baudRateComboBox.currentText()),
                    timeout=UPDATE_PERIOD / 1000.0,
                )
                if (self.serial is None) or (not self.serial.is_open):
                    raise serial.SerialException("Unexpected error")
                logger.debug(f"Serial connected to {self.serial}")
            except (ValueError, serial.SerialException) as e:
                # noinspection PyArgumentList
                QMessageBox.critical(self, "ERROR", str(e))
                return
            self.serial.reset_output_buffer()
            self.serial.reset_input_buffer()
            # as advised in https://pyserial.readthedocs.io/en/latest/shortintro.html#eol
            # noinspection PyTypeChecker
            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial, self.serial))

            self.serialConnectButton.setChecked(True)
            self.serialPortsComboBox.setEnabled(False)
            self.refreshSerialButton.setEnabled(False)
            self.baudRateComboBox.setEnabled(False)
            self.infoGroupBox.setEnabled(True)
            self.startButton.setEnabled(True)
            self.statusbar.showMessage(
                f"Connected to {self.serial.port} ({self.serial.baudrate} bauds)"
            )
        else:
            # button is already checked, disconnect
            logger.debug(f"Closing serial port {self.serial}")
            if self.timer.isActive():
                logger.debug("Acquisition in progress... stopping")
                self.stop()
            if self.serial is not None:
                self.serial.close()
            self.serialConnectButton.setChecked(False)
            self.serialPortsComboBox.setEnabled(True)
            self.refreshSerialButton.setEnabled(True)
            self.baudRateComboBox.setEnabled(True)
            self.infoGroupBox.setEnabled(False)
            self.startButton.setEnabled(False)
            self.statusbar.clearMessage()

    def update(self) -> None:
        logging.debug(f"Reading data from {self.serial}")
        line = self.sio.readline()
        logging.debug(f">> {line}")
        if len(line) > 0:
            self.serialOutputWidget.appendPlainText(line[:-1])
            self.file.write(line)

        try:
            _, _, x, y = line.split(",")
            x, y = map(float, [x, y])
            self.data = np.append(self.data, [[x, y]], axis=0)
            self.curve.setData(self.data)
        except ValueError:
            logger.debug(f"Failed to convert {line} to float")
            pass  # drop line if it cannot be converted to float

    def list_serial_ports(self):
        self.serial_ports = sorted(list_ports.comports())
        serial_list = [f"{dev.device} ({dev.description})" for dev in self.serial_ports]
        self.serialPortsComboBox.clear()
        for label, obj in zip(serial_list, self.serial_ports):
            self.serialPortsComboBox.addItem(label, obj)

    def browse_root_path(self):
        dialog = QFileDialog()
        # noinspection PyArgumentList
        foo_dir = dialog.getExistingDirectory(self, "Select the directory")
        foo_dir = Path(foo_dir).resolve()
        self.rootPath = foo_dir
        self.rootPathEdit.setText(foo_dir.as_posix())

    def clear(self):
        self.serialOutputWidget.clear()
        self.data = np.ndarray(shape=(0, 2))
        self.curve.clear()
        self.plotItem.setTitle("")
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

    def stop(self):
        self.timer.stop()
        if self.file is not None:
            self.file.close()

        self.file = None

        self.infoGroupBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

        # noinspection PyBroadException
        try:
            exporter = pg.exporters.ImageExporter(self.plotItem)
            p = self.rootPath / f"{self.basename}.png"
            exporter.export(p.as_posix())
        except Exception as e:  # I'm not sure what kind of exception can be raised by the exported
            QMessageBox.Warning(
                self, "Cannot save image", f"The image could not be saved\n{str(e)}"
            )

    def start(self):
        if len(self.subjectIDEdit.text()) == 0:
            print("\a")  # bell
            self.subjectIDEdit.setStyleSheet(self.subjectIDMissingStylesheet)
            logger.debug("Subject ID is missing, please correct")
            return

        # we are ready to go at this point
        self.clear()

        date = datetime.date.today().strftime(DATE_FORMAT)
        self.basename = f"{date}_{self.subjectIDEdit.text()}"
        filename = self.basename + ".csv"
        path = self.rootPath / filename
        if path.is_file():
            # noinspection PyArgumentList
            ok = QMessageBox.warning(
                self,
                "File exists",
                f'File "{filename}" already exists in {path.as_posix()}. Do you want to erase it?',
                buttons=QMessageBox.Yes | QMessageBox.No,
            )
            if ok == QMessageBox.No:
                self.stop()
                return
        self.plotItem.setTitle(filename)
        try:
            self.file = open(path, "w")
        except OSError:
            # noinspection PyArgumentList
            QMessageBox.critical(
                self, "ERROR", f"cannot open file {self.file} for writing"
            )
            return

        self.infoGroupBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.timer.start(0)

    def subject_id_edited(self):
        self.subjectIDEdit.setStyleSheet("")

    def action_open_file(self, _):
        filename = self.browse_file()
        if len(filename) == 0:
            return
        self.load_file(filename)

    def load_file(self, filename):
        try:
            data = np.genfromtxt(filename, delimiter=",", usecols=[2, 3])
            if len(data) > 0:
                self.data = data
                self.curve.setData(data)
                self.plotItem.setTitle(filename)
                with open(filename, 'r') as f:
                    self.serialOutputWidget.setPlainText(f.read())
        except Exception as e:
            # noinspection PyArgumentList
            QMessageBox.warning(self, "ERROR", f"Could not read file {filename}\n{str(e)}")
            logger.debug(f"Failed to read data from file <{filename}>\n{str(e)}")

    def browse_file(self):
        dialog = QFileDialog()
        root = self.rootPath
        if root is None:
            root = Path.cwd()
        # noinspection PyArgumentList
        filename, _ = dialog.getOpenFileName(
            self, caption="Open data file", directory=root.as_posix(), filter="Text files (*.txt *.csv);;All files (*)"
        )
        filename = Path(filename).resolve().as_posix()
        return filename

    def closeEvent(self, event: QCloseEvent):
        logger.debug("in closeEvent()")
        if self.timer.isActive():
            self.timer.stop()
        if self.file is not None:
            self.file.close()
        if self.serial is not None:
            self.serial.close()
        event.accept()


if __name__ == "__main__":
    logging.debug("in main.")
    app = QApplication([])
    win = MainWindow()
    win.setWindowTitle("Torque Meter")
    win.show()
    app.exec()
