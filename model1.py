# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(603, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(27, 51, 89);")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.gridLayout_4 = QGridLayout(self.MainPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.frame_5 = QFrame(self.MainPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(232, 32, 112);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(1677, 1677))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ToReturn = QPushButton(self.frame)
        self.ToReturn.setObjectName(u"ToReturn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToReturn.sizePolicy().hasHeightForWidth())
        self.ToReturn.setSizePolicy(sizePolicy1)
        self.ToReturn.setMinimumSize(QSize(100, 20))
        self.ToReturn.setMaximumSize(QSize(100, 20))
        self.ToReturn.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_3.addWidget(self.ToReturn, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.ToLoan = QPushButton(self.frame)
        self.ToLoan.setObjectName(u"ToLoan")
        sizePolicy1.setHeightForWidth(self.ToLoan.sizePolicy().hasHeightForWidth())
        self.ToLoan.setSizePolicy(sizePolicy1)
        self.ToLoan.setMinimumSize(QSize(100, 20))
        self.ToLoan.setMaximumSize(QSize(100, 20))
        self.ToLoan.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_3.addWidget(self.ToLoan, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.ToHistory = QPushButton(self.frame)
        self.ToHistory.setObjectName(u"ToHistory")
        sizePolicy1.setHeightForWidth(self.ToHistory.sizePolicy().hasHeightForWidth())
        self.ToHistory.setSizePolicy(sizePolicy1)
        self.ToHistory.setMinimumSize(QSize(100, 20))
        self.ToHistory.setMaximumSize(QSize(100, 20))
        self.ToHistory.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_3.addWidget(self.ToHistory, 6, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.Loan = QWidget()
        self.Loan.setObjectName(u"Loan")
        self.gridLayout_6 = QGridLayout(self.Loan)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_2 = QFrame(self.Loan)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(1677, 1677))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setMidLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 477, 256))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 1, 8, 1, 1)

        self.FromLoan = QPushButton(self.frame_2)
        self.FromLoan.setObjectName(u"FromLoan")
        sizePolicy1.setHeightForWidth(self.FromLoan.sizePolicy().hasHeightForWidth())
        self.FromLoan.setSizePolicy(sizePolicy1)
        self.FromLoan.setMinimumSize(QSize(100, 20))
        self.FromLoan.setMaximumSize(QSize(100, 20))
        self.FromLoan.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_5.addWidget(self.FromLoan, 4, 8, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(40)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 40))
        self.textEdit.setMaximumSize(QSize(16777215, 40))
        self.textEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")

        self.gridLayout_5.addWidget(self.textEdit, 0, 8, 1, 1)

        self.DoLoan = QPushButton(self.frame_2)
        self.DoLoan.setObjectName(u"DoLoan")
        sizePolicy1.setHeightForWidth(self.DoLoan.sizePolicy().hasHeightForWidth())
        self.DoLoan.setSizePolicy(sizePolicy1)
        self.DoLoan.setMinimumSize(QSize(100, 20))
        self.DoLoan.setMaximumSize(QSize(100, 20))
        self.DoLoan.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_5.addWidget(self.DoLoan, 3, 8, 1, 1, Qt.AlignRight)


        self.gridLayout_6.addWidget(self.frame_2, 2, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.Loan)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 32, 112);")

        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.Loan)
        self.Return = QWidget()
        self.Return.setObjectName(u"Return")
        self.gridLayout_8 = QGridLayout(self.Return)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_3 = QFrame(self.Return)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(1677, 1677))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(0)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 477, 256))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_7.addWidget(self.scrollArea_2, 1, 8, 1, 1)

        self.FromReturn = QPushButton(self.frame_3)
        self.FromReturn.setObjectName(u"FromReturn")
        sizePolicy1.setHeightForWidth(self.FromReturn.sizePolicy().hasHeightForWidth())
        self.FromReturn.setSizePolicy(sizePolicy1)
        self.FromReturn.setMinimumSize(QSize(100, 20))
        self.FromReturn.setMaximumSize(QSize(100, 20))
        self.FromReturn.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_7.addWidget(self.FromReturn, 4, 8, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.DoReturn = QPushButton(self.frame_3)
        self.DoReturn.setObjectName(u"DoReturn")
        sizePolicy1.setHeightForWidth(self.DoReturn.sizePolicy().hasHeightForWidth())
        self.DoReturn.setSizePolicy(sizePolicy1)
        self.DoReturn.setMinimumSize(QSize(100, 20))
        self.DoReturn.setMaximumSize(QSize(100, 20))
        self.DoReturn.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_7.addWidget(self.DoReturn, 3, 8, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.textEdit_2 = QTextEdit(self.frame_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy2.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy2)
        self.textEdit_2.setMinimumSize(QSize(0, 40))
        self.textEdit_2.setMaximumSize(QSize(16777215, 40))
        self.textEdit_2.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")

        self.gridLayout_7.addWidget(self.textEdit_2, 0, 8, 1, 1)


        self.gridLayout_8.addWidget(self.frame_3, 2, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_9, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.Return)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 32, 112);")

        self.gridLayout_8.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.Return)
        self.History = QWidget()
        self.History.setObjectName(u"History")
        self.gridLayout = QGridLayout(self.History)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.History)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(1677, 1677))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(0)
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.DoHistory = QPushButton(self.frame_4)
        self.DoHistory.setObjectName(u"DoHistory")
        sizePolicy1.setHeightForWidth(self.DoHistory.sizePolicy().hasHeightForWidth())
        self.DoHistory.setSizePolicy(sizePolicy1)
        self.DoHistory.setMinimumSize(QSize(100, 20))
        self.DoHistory.setMaximumSize(QSize(100, 20))
        self.DoHistory.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_9.addWidget(self.DoHistory, 3, 7, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.scrollArea_3 = QScrollArea(self.frame_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 477, 256))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_9.addWidget(self.scrollArea_3, 1, 7, 1, 1)

        self.FromHistory = QPushButton(self.frame_4)
        self.FromHistory.setObjectName(u"FromHistory")
        sizePolicy1.setHeightForWidth(self.FromHistory.sizePolicy().hasHeightForWidth())
        self.FromHistory.setSizePolicy(sizePolicy1)
        self.FromHistory.setMinimumSize(QSize(100, 20))
        self.FromHistory.setMaximumSize(QSize(100, 20))
        self.FromHistory.setStyleSheet(u"background-color: rgb(75, 188, 197);\n"
"")

        self.gridLayout_9.addWidget(self.FromHistory, 4, 7, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.textEdit_3 = QTextEdit(self.frame_4)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy2.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy2)
        self.textEdit_3.setMinimumSize(QSize(0, 40))
        self.textEdit_3.setMaximumSize(QSize(16777215, 40))
        self.textEdit_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 2px;\n"
"border-color: rgb(0, 150, 179);")

        self.gridLayout_9.addWidget(self.textEdit_3, 0, 7, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_11, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.History)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"border-color: rgb(232, 32, 112);")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.History)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 603, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToReturn.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.ToLoan.setText(QCoreApplication.translate("MainWindow", u"Loan", None))
        self.ToHistory.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.FromLoan.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.DoLoan.setText(QCoreApplication.translate("MainWindow", u"Loan", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Loan", None))
        self.FromReturn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.DoReturn.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.DoHistory.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.FromHistory.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"History", None))
    # retranslateUi

