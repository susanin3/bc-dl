# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 797, 405))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_url = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_url.setObjectName("le_url")
        self.horizontalLayout_2.addWidget(self.le_url)
        self.tb_url = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.tb_url.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tb_url.setObjectName("tb_url")
        self.horizontalLayout_2.addWidget(self.tb_url)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_location = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_location.setObjectName("le_location")
        self.horizontalLayout_4.addWidget(self.le_location)
        self.tb_location = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.tb_location.setObjectName("tb_location")
        self.horizontalLayout_4.addWidget(self.tb_location)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cb_lyrics = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_lyrics.setObjectName("cb_lyrics")
        self.horizontalLayout_3.addWidget(self.cb_lyrics)
        self.cb_sort = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_sort.setObjectName("cb_sort")
        self.horizontalLayout_3.addWidget(self.cb_sort)
        self.cb_localize = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_localize.setObjectName("cb_localize")
        self.horizontalLayout_3.addWidget(self.cb_localize)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pb_downloading = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.pb_downloading.setProperty("value", 0)
        self.pb_downloading.setObjectName("pb_downloading")
        self.verticalLayout.addWidget(self.pb_downloading)
        self.textbr_logs = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbr_logs.sizePolicy().hasHeightForWidth())
        self.textbr_logs.setSizePolicy(sizePolicy)
        self.textbr_logs.setObjectName("textbr_logs")
        self.verticalLayout.addWidget(self.textbr_logs)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_download = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_download.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_7.addWidget(self.btn_download)
        self.btn_stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_7.addWidget(self.btn_stop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bandcamp downloader GUI"))
        self.le_url.setPlaceholderText(_translate("MainWindow", "URL for artist | album | track or path to file with urls"))
        self.tb_url.setText(_translate("MainWindow", "..."))
        self.le_location.setPlaceholderText(_translate("MainWindow", "Save location"))
        self.tb_location.setText(_translate("MainWindow", "..."))
        self.cb_lyrics.setText(_translate("MainWindow", "Create lyrics files"))
        self.cb_sort.setText(_translate("MainWindow", "Sort"))
        self.cb_localize.setText(_translate("MainWindow", "Localize"))
        self.textbr_logs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#d31a2d;\">This is a BETA version of the GUI, so it may not work correctly!</span></p></body></html>"))