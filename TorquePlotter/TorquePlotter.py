# TorquePlotter.py
# Quick and dirty GUI for reading incoming serial port data from the Torque Meter
# plotting the data and saving it as csv file
import argparse
import logging
import typing
from io import StringIO
from pathlib import Path

import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters
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
    QApplication, QAction, QSpinBox, QButtonGroup, QDoubleSpinBox, QRadioButton,
)
from serial.tools import list_ports

UPDATE_PERIOD = 100  # in ms
FILE_NAME_TEMPLATE = '{ID}_P{Age:d}_{Limb}_{Speed}s{Comments}'

logger = logging.getLogger("TorquePlotter")
handler = logging.StreamHandler()
# noinspection SpellCheckingInspection
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
LOGGING_LEVELS = [logging.NOTSET, logging.WARNING, logging.INFO, logging.DEBUG]


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
    subjectAgeSpinBox: QSpinBox
    limbButtonGroup: QButtonGroup
    subjectLimbFLRadioButton: QRadioButton
    subjectLimbFRRadioButton: QRadioButton
    subjectLimbHLRadioButton: QRadioButton
    subjectLimbHRRadioButton: QRadioButton
    subjectSpeedSpinBox: QDoubleSpinBox
    subjectCommentsEdit: QLineEdit
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
        uic.loadUi(Path(__file__).parent.resolve() / "MainWindow.ui", self)  # Load the .ui file

        self.subjectIDMissingStylesheet = "background:red"

        self.basename = ""
        self.serial = None
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

        self.LIMB_BUTTON_MAPPING = {self.subjectLimbFLRadioButton: 'FL', self.subjectLimbFRRadioButton: 'FR',
                                    self.subjectLimbHLRadioButton: 'HL', self.subjectLimbHRRadioButton: 'HR'}

        self.plotItem: pg.PlotItem = self.plotView.getPlotItem()
        self.plotItem.setLabels(left="Force (gf)", bottom="Angle (deg)")
        self.plotItem.showGrid(x=True, y=True, alpha=0.5)
        self.curve = self.plotItem.plot(symbol="o")
        self.data = np.ndarray(shape=(0, 2))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.stop()

        self._serial_buffer = ''

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

    def process_incoming_data(self, in_data, sep='\n'):
        # since we are reading the data in chunks, there is no guarantee
        # that we captured full lines, so we use a buffer and use only the full lines present in the buffer,
        # the rest remaining the buffer for the next update() call
        self._serial_buffer += in_data
        # logger.debug(f"_serial_buffer = {self._serial_buffer}")
        out_data, sep, after = self._serial_buffer.rpartition(sep)
        self._serial_buffer = after
        # logger.debug(f"kep '{self._serial_buffer}' in buffer, returning '{out_data}'")
        return out_data

    def update(self) -> None:
        if self.serial.in_waiting > 0:
            logger.debug(f"Reading data from {self.serial}")
            out_data = self.process_incoming_data(self.serial.read(self.serial.in_waiting).decode())
            if len(out_data) > 0:
                self.serialOutputWidget.appendPlainText(out_data)
                self.file.write(out_data)

                try:
                    data = np.genfromtxt(StringIO(out_data), delimiter=',', usecols=[2, 3])
                    # logger.debug(f"Converted to numpy: {data}")
                    self.data = np.append(self.data, np.atleast_2d(data), axis=0)
                    self.curve.setData(self.data)
                except ValueError as e:
                    logger.debug(f"Failed to convert {out_data}: {e}")
                    pass  # drop data if it cannot be converted to float

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
            p = self.rootPath / (self.basename+'.png')
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

        filename = FILE_NAME_TEMPLATE.format(ID=self.subjectIDEdit.text(),
                                             Age=self.subjectAgeSpinBox.value(),
                                             Limb=self.LIMB_BUTTON_MAPPING[self.limbButtonGroup.checkedButton()],
                                             Speed=self.subjectSpeedSpinBox.value(),
                                             Comments=self.get_subject_comments(),
                                             )
        self.basename = filename
        filename += '.csv'
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

    def get_subject_comments(self):
        txt = self.subjectCommentsEdit.text()
        if len(txt) > 0:
            txt = txt.replace(' ', '-')
            txt = txt.replace('_', '-')
            txt = '_' + txt
        return txt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase verbosity of output (can be "
             "repeated to increase verbosity further)",
    )
    parser.add_argument(
        "--log-file",
        help="file in which the log is written. "
             "If absent or None, log is directed to stdout",
        default=None,
    )
    args = parser.parse_args()

    level = LOGGING_LEVELS[
        min(args.verbose, len(LOGGING_LEVELS) - 1)
    ]  # cap to last level index
    logger.setLevel(level=level)

    app = QApplication([])
    win = MainWindow()
    win.setWindowTitle("Torque Meter")
    win.show()
    app.exec()
