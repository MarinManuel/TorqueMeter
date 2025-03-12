# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.startHereGroupBox = QGroupBox(self.frame_2)
        self.startHereGroupBox.setObjectName(u"startHereGroupBox")
        self.formLayout_2 = QFormLayout(self.startHereGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.openResultFileButton = QPushButton(self.startHereGroupBox)
        self.openResultFileButton.setObjectName(u"openResultFileButton")
        icon = QIcon()
        icon.addFile(u":/icons/summary", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openResultFileButton.setIcon(icon)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.openResultFileButton)

        self.summaryFilePathEdit = QLabel(self.startHereGroupBox)
        self.summaryFilePathEdit.setObjectName(u"summaryFilePathEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.summaryFilePathEdit)

        self.openDataFolderButton = QPushButton(self.startHereGroupBox)
        self.openDataFolderButton.setObjectName(u"openDataFolderButton")
        self.openDataFolderButton.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/open_folder", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openDataFolderButton.setIcon(icon1)
        self.openDataFolderButton.setIconSize(QSize(16, 16))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.openDataFolderButton)

        self.dataFolderPathEdit = QLabel(self.startHereGroupBox)
        self.dataFolderPathEdit.setObjectName(u"dataFolderPathEdit")
        self.dataFolderPathEdit.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.dataFolderPathEdit)

        self.skipAlreadyAnalyzedCheckBox = QCheckBox(self.startHereGroupBox)
        self.skipAlreadyAnalyzedCheckBox.setObjectName(u"skipAlreadyAnalyzedCheckBox")
        self.skipAlreadyAnalyzedCheckBox.setChecked(True)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.skipAlreadyAnalyzedCheckBox)


        self.verticalLayout.addWidget(self.startHereGroupBox)

        self.fileInfoGroupBox = QGroupBox(self.frame_2)
        self.fileInfoGroupBox.setObjectName(u"fileInfoGroupBox")
        self.fileInfoGroupBox.setEnabled(False)
        self.formLayout = QFormLayout(self.fileInfoGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.fileInfoGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.expDateEdit = QDateEdit(self.fileInfoGroupBox)
        self.expDateEdit.setObjectName(u"expDateEdit")
        self.expDateEdit.setDateTime(QDateTime(QDate(2022, 5, 12), QTime(0, 0, 0)))
        self.expDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.expDateEdit)

        self.label = QLabel(self.fileInfoGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.rabbitIDEdit = QLineEdit(self.fileInfoGroupBox)
        self.rabbitIDEdit.setObjectName(u"rabbitIDEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rabbitIDEdit)

        self.label_2 = QLabel(self.fileInfoGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.rabbitAgeSpinBox = QSpinBox(self.fileInfoGroupBox)
        self.rabbitAgeSpinBox.setObjectName(u"rabbitAgeSpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rabbitAgeSpinBox)

        self.label_4 = QLabel(self.fileInfoGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.fileInfoGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.expSpeedSpinBox = QDoubleSpinBox(self.fileInfoGroupBox)
        self.expSpeedSpinBox.setObjectName(u"expSpeedSpinBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.expSpeedSpinBox)

        self.label_6 = QLabel(self.fileInfoGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.expCommentEdit = QLineEdit(self.fileInfoGroupBox)
        self.expCommentEdit.setObjectName(u"expCommentEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.expCommentEdit)

        self.rabbitLimbEdit = QLineEdit(self.fileInfoGroupBox)
        self.rabbitLimbEdit.setObjectName(u"rabbitLimbEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rabbitLimbEdit)


        self.verticalLayout.addWidget(self.fileInfoGroupBox)

        self.analysisGroupBox = QGroupBox(self.frame_2)
        self.analysisGroupBox.setObjectName(u"analysisGroupBox")
        self.analysisGroupBox.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.analysisGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cyclesToKeepEdit = QLineEdit(self.analysisGroupBox)
        self.cyclesToKeepEdit.setObjectName(u"cyclesToKeepEdit")
        self.cyclesToKeepEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.cyclesToKeepEdit, 1, 1, 1, 2)

        self.label_9 = QLabel(self.analysisGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.removeOutliersCheckBox = QCheckBox(self.analysisGroupBox)
        self.removeOutliersCheckBox.setObjectName(u"removeOutliersCheckBox")

        self.gridLayout_2.addWidget(self.removeOutliersCheckBox, 0, 0, 1, 2)

        self.rejectFileButton = QPushButton(self.analysisGroupBox)
        self.rejectFileButton.setObjectName(u"rejectFileButton")
        self.rejectFileButton.setStyleSheet(u"QPushButton{ background: rgb(255, 170, 127);}\n"
"QPushButton:checked{ background: rgb(255, 0, 0);}")
        self.rejectFileButton.setCheckable(True)
        self.rejectFileButton.setChecked(False)
        self.rejectFileButton.setFlat(False)

        self.gridLayout_2.addWidget(self.rejectFileButton, 2, 0, 1, 3)

        self.outlierThresholdSpinBox = QDoubleSpinBox(self.analysisGroupBox)
        self.outlierThresholdSpinBox.setObjectName(u"outlierThresholdSpinBox")
        self.outlierThresholdSpinBox.setEnabled(False)
        self.outlierThresholdSpinBox.setDecimals(2)
        self.outlierThresholdSpinBox.setValue(2.000000000000000)

        self.gridLayout_2.addWidget(self.outlierThresholdSpinBox, 0, 2, 1, 1)

        self.validateButton = QPushButton(self.analysisGroupBox)
        self.validateButton.setObjectName(u"validateButton")
        self.validateButton.setEnabled(False)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(127, 255, 191, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(106, 212, 159, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(42, 85, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(57, 113, 85, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(170, 212, 191, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(42, 85, 64, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(110, 221, 165, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.validateButton.setPalette(palette)

        self.gridLayout_2.addWidget(self.validateButton, 3, 0, 1, 3)


        self.verticalLayout.addWidget(self.analysisGroupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.rightPanelGroupBox = QGroupBox(self.centralwidget)
        self.rightPanelGroupBox.setObjectName(u"rightPanelGroupBox")
        self.rightPanelGroupBox.setEnabled(True)
        self.rightPanelLayout = QVBoxLayout(self.rightPanelGroupBox)
        self.rightPanelLayout.setObjectName(u"rightPanelLayout")
        self.rightPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.currentFileFrame = QFrame(self.rightPanelGroupBox)
        self.currentFileFrame.setObjectName(u"currentFileFrame")
        self.currentFileFrame.setEnabled(True)
        self.currentFileFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.currentFileFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.currentFileFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prevFileButton = QPushButton(self.currentFileFrame)
        self.prevFileButton.setObjectName(u"prevFileButton")
        self.prevFileButton.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/previous", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevFileButton.setIcon(icon2)
        self.prevFileButton.setIconSize(QSize(32, 32))
        self.prevFileButton.setFlat(True)

        self.horizontalLayout.addWidget(self.prevFileButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.currentFileFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_11)

        self.currentFileSpinBox = QSpinBox(self.currentFileFrame)
        self.currentFileSpinBox.setObjectName(u"currentFileSpinBox")
        self.currentFileSpinBox.setEnabled(True)
        self.currentFileSpinBox.setMaximum(0)

        self.horizontalLayout.addWidget(self.currentFileSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.nextFileButton = QPushButton(self.currentFileFrame)
        self.nextFileButton.setObjectName(u"nextFileButton")
        self.nextFileButton.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/next", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextFileButton.setIcon(icon3)
        self.nextFileButton.setIconSize(QSize(32, 32))
        self.nextFileButton.setFlat(True)

        self.horizontalLayout.addWidget(self.nextFileButton)


        self.rightPanelLayout.addWidget(self.currentFileFrame)


        self.horizontalLayout_2.addWidget(self.rightPanelGroupBox)

        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.openResultFileButton, self.openDataFolderButton)
        QWidget.setTabOrder(self.openDataFolderButton, self.skipAlreadyAnalyzedCheckBox)
        QWidget.setTabOrder(self.skipAlreadyAnalyzedCheckBox, self.prevFileButton)
        QWidget.setTabOrder(self.prevFileButton, self.currentFileSpinBox)
        QWidget.setTabOrder(self.currentFileSpinBox, self.nextFileButton)
        QWidget.setTabOrder(self.nextFileButton, self.expDateEdit)
        QWidget.setTabOrder(self.expDateEdit, self.rabbitIDEdit)
        QWidget.setTabOrder(self.rabbitIDEdit, self.rabbitAgeSpinBox)
        QWidget.setTabOrder(self.rabbitAgeSpinBox, self.rabbitLimbEdit)
        QWidget.setTabOrder(self.rabbitLimbEdit, self.expSpeedSpinBox)
        QWidget.setTabOrder(self.expSpeedSpinBox, self.expCommentEdit)
        QWidget.setTabOrder(self.expCommentEdit, self.removeOutliersCheckBox)
        QWidget.setTabOrder(self.removeOutliersCheckBox, self.outlierThresholdSpinBox)
        QWidget.setTabOrder(self.outlierThresholdSpinBox, self.cyclesToKeepEdit)
        QWidget.setTabOrder(self.cyclesToKeepEdit, self.rejectFileButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startHereGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Start Here", None))
        self.openResultFileButton.setText("")
        self.summaryFilePathEdit.setText(QCoreApplication.translate("MainWindow", u"Result file...", None))
        self.openDataFolderButton.setText("")
        self.dataFolderPathEdit.setText(QCoreApplication.translate("MainWindow", u"Load data files...", None))
        self.skipAlreadyAnalyzedCheckBox.setText(QCoreApplication.translate("MainWindow", u"Skip already analyzed files", None))
        self.fileInfoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"File Info", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Exp Date", None))
        self.expDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rabbit ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rabbit Age", None))
        self.rabbitAgeSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Limb", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"comment", None))
        self.analysisGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cycles", None))
        self.removeOutliersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Remove &Outliers", None))
#if QT_CONFIG(shortcut)
        self.removeOutliersCheckBox.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.rejectFileButton.setText(QCoreApplication.translate("MainWindow", u"&Reject File", None))
#if QT_CONFIG(shortcut)
        self.rejectFileButton.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.outlierThresholdSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"> ", None))
        self.outlierThresholdSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" \u03c3", None))
        self.validateButton.setText(QCoreApplication.translate("MainWindow", u"V&alidate && Next", None))
#if QT_CONFIG(statustip)
        self.prevFileButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Load previous file", None))
#endif // QT_CONFIG(statustip)
        self.prevFileButton.setText("")
#if QT_CONFIG(shortcut)
        self.prevFileButton.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"file:", None))
        self.currentFileSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" / 0", None))
#if QT_CONFIG(tooltip)
        self.nextFileButton.setToolTip(QCoreApplication.translate("MainWindow", u"Load next file", None))
#endif // QT_CONFIG(tooltip)
        self.nextFileButton.setText("")
#if QT_CONFIG(shortcut)
        self.nextFileButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

