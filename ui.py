# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Thu Sep 26 14:29:27 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QStatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 351)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 40, 200, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setStyleSheet("QPushButton::hover{background-color: rgb(192, 225, 255);}\n"
                                      "QPushButton{ background-color: rgb(230, 241, 255);"
                                      " border-radius: 5px; border: 1px solid rgb(190, 220, 255)}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 250, 27))
        self.lineEdit.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 68, 17))
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 120, 250, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 260, 200, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setStyleSheet("QPushButton::hover{background-color: rgb(192, 225, 255);}\n"
                                        "QPushButton{ background-color: rgb(230, 241, 255);"
                                        " border-radius: 5px; border: 1px solid rgb(190, 220, 255)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 140, 250, 27))
        self.lineEdit_3.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 261, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 40, 250, 27))
        self.lineEdit_4.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 210, 250, 27))
        self.lineEdit_5.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 190, 201, 17))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Настройка роутера", None))
        self.pushButton.setText(QApplication.translate("MainWindow", "Подключиться", None))
        self.label.setText(QApplication.translate("MainWindow", "SSID", None))
        self.label_2.setText(QApplication.translate("MainWindow", "Пароль (минимум 8 символов)", None))
        self.pushButton_2.setText(QApplication.translate("MainWindow", "Настроить", None))
        self.label_3.setText(QApplication.translate("MainWindow", "Модель подключенного устройства", None))
        self.label_5.setText(QApplication.translate("MainWindow", "Пароль доступа к роутеру", None))

