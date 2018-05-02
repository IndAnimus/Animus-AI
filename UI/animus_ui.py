#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 4th May 2018        #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul                                   #
####################################################################
# Animus GUI environment
# Form implementation generated from reading ui file 'animus.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AnimusAI(object):
    def setupUi(self, AnimusAI):
        AnimusAI.setObjectName(_fromUtf8("AnimusAI"))
        AnimusAI.resize(640, 480)
        self.centralwidget = QtGui.QWidget(AnimusAI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 621, 421))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.dashboard = QtGui.QWidget()
        self.dashboard.setObjectName(_fromUtf8("dashboard"))
        self.Send = QtGui.QPushButton(self.dashboard)
        self.Send.setGeometry(QtCore.QRect(480, 320, 111, 41))
        self.Send.setObjectName(_fromUtf8("Send"))
        self.label = QtGui.QLabel(self.dashboard)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.Message = QtGui.QTextEdit(self.dashboard)
        self.Message.setGeometry(QtCore.QRect(10, 290, 461, 75))
        self.Message.setObjectName(_fromUtf8("Message"))
        self.Start = QtGui.QPushButton(self.dashboard)
        self.Start.setGeometry(QtCore.QRect(478, 280, 111, 27))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.tabWidget.addTab(self.dashboard, _fromUtf8(""))
        self.help = QtGui.QWidget()
        self.help.setObjectName(_fromUtf8("help"))
        self.label_2 = QtGui.QLabel(self.help)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 551, 301))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.help, _fromUtf8(""))
        self.account = QtGui.QWidget()
        self.account.setObjectName(_fromUtf8("account"))
        self.Email = QtGui.QTextEdit(self.account)
        self.Email.setGeometry(QtCore.QRect(110, 80, 481, 31))
        self.Email.setObjectName(_fromUtf8("Email"))
        self.label_3 = QtGui.QLabel(self.account)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EmailPass = QtGui.QTextEdit(self.account)
        self.EmailPass.setGeometry(QtCore.QRect(110, 120, 261, 31))
        self.EmailPass.setObjectName(_fromUtf8("EmailPass"))
        self.label_4 = QtGui.QLabel(self.account)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.account)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 101, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Wit = QtGui.QTextEdit(self.account)
        self.Wit.setGeometry(QtCore.QRect(140, 160, 451, 31))
        self.Wit.setObjectName(_fromUtf8("Wit"))
        self.Wolfram = QtGui.QTextEdit(self.account)
        self.Wolfram.setGeometry(QtCore.QRect(140, 200, 451, 31))
        self.Wolfram.setObjectName(_fromUtf8("Wolfram"))
        self.label_6 = QtGui.QLabel(self.account)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 68, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Name = QtGui.QTextEdit(self.account)
        self.Name.setGeometry(QtCore.QRect(110, 40, 381, 31))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.label_7 = QtGui.QLabel(self.account)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 121, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.account)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 161, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Weather = QtGui.QTextEdit(self.account)
        self.Weather.setGeometry(QtCore.QRect(180, 240, 411, 31))
        self.Weather.setObjectName(_fromUtf8("Weather"))
        self.Save = QtGui.QPushButton(self.account)
        self.Save.setGeometry(QtCore.QRect(450, 290, 111, 51))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.tabWidget.addTab(self.account, _fromUtf8(""))
        AnimusAI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AnimusAI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAnimus_AI = QtGui.QMenu(self.menubar)
        self.menuAnimus_AI.setObjectName(_fromUtf8("menuAnimus_AI"))
        AnimusAI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AnimusAI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AnimusAI.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAnimus_AI.menuAction())

        self.retranslateUi(AnimusAI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.Send, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear)
        QtCore.QObject.connect(self.Save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Wolfram.clear)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Message.clear)
        QtCore.QMetaObject.connectSlotsByName(AnimusAI)
        AnimusAI.setTabOrder(self.tabWidget, self.Message)
        AnimusAI.setTabOrder(self.Message, self.Send)
        AnimusAI.setTabOrder(self.Send, self.Email)
        AnimusAI.setTabOrder(self.Email, self.EmailPass)
        AnimusAI.setTabOrder(self.EmailPass, self.Wolfram)
        AnimusAI.setTabOrder(self.Wolfram, self.Wit)
        AnimusAI.setTabOrder(self.Wit, self.Save)
        AnimusAI.setTabOrder(self.Save, self.Name)
        AnimusAI.setTabOrder(self.Name, self.Weather)

    def retranslateUi(self, AnimusAI):
        AnimusAI.setWindowTitle(_translate("AnimusAI", "Animus AI", None))
        self.Send.setText(_translate("AnimusAI", "OK", None))
        self.label.setText(_translate("AnimusAI", "Animus AI", None))
        self.Start.setText(_translate("AnimusAI", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dashboard), _translate("AnimusAI", "Animus Dashboard", None))
        self.label_2.setText(_translate("AnimusAI", "Animus has been developed with\n"
"majorly open source Machine\n"
"Learning and Natural Language\n"
"Processing Components. Animus is\n"
"the only AI assistant in the market\n"
"that has the ability to understand\n"
"and interact with visual data.\n"
"Animus understands your needs\n"
"and learns from your activities. We\n"
"have made animus more useful by\n"
"implementing many skills like\n"
"Hailing an Uber ride, reading out\n"
"your mail and Searching the web\n"
"for content.\n"
"Animus can run on even a\n"
"raspberry pi and we hope to port it\n"
"to windows very soon.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.help), _translate("AnimusAI", "Help", None))
        self.label_3.setText(_translate("AnimusAI", "Email-ID:", None))
        self.label_4.setText(_translate("AnimusAI", "Password:", None))
        self.label_5.setText(_translate("AnimusAI", "Wit.Ai API Key:", None))
        self.label_6.setText(_translate("AnimusAI", "Name:", None))
        self.label_7.setText(_translate("AnimusAI", "Wolfram API Key:", None))
        self.label_8.setText(_translate("AnimusAI", "OpenWeather API Key:", None))
        self.Save.setText(_translate("AnimusAI", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account), _translate("AnimusAI", "Account", None))
        self.menuAnimus_AI.setTitle(_translate("AnimusAI", "Animus AI", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AnimusAI = QtGui.QMainWindow()
    ui = Ui_AnimusAI()
    ui.setupUi(AnimusAI)
    AnimusAI.show()
    sys.exit(app.exec_())
