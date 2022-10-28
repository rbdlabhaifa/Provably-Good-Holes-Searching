from tkinter import filedialog

import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from tkinter import *

from matplotlib import pyplot as plt

from algo import algorithm
import PIL
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 70, 121, 51))
        self.label.setObjectName("label")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(250, 120, 75, 23))
        self.browse.setObjectName("browse")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.save.setObjectName("save")

        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(250, 200, 75, 23))
        self.run.setObjectName("run")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 310, 151, 16))
        self.label_2.setObjectName(("label_2"))

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 160, 271, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(235, 230, 100, 31))
        self.textEdit2.setObjectName("textEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse.clicked.connect(self.browseEvent)
        self.run.clicked.connect(self.loadEvent)
        self.save.clicked.connect(self.saveEvent)
        self.img = None
        self.result = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1. CHOOSE IMAGE\n"
"2. RUN"))
        self.browse.setText(_translate("MainWindow", "BROWSE"))
        self.run.setText(_translate("MainWindow", "RUN"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.textEdit2.setText(_translate("MainWindow", "image_Name.tiff"))

    def browseEvent(self):
        fName = QFileDialog.getOpenFileName(None, 'Open file')
        self.textEdit.setText(fName[0])
        self.img = cv2.imread(fName[0])
        # self.img = Image.open(fName[0])

    def loadEvent(self):

        ret, self.img = algorithm(self.img)
        ret -= 1
        self.label_2.setText(f"{ret} holes found")


    def saveEvent(self):
        fName = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        name = self.textEdit2.toPlainText()
        try:
            plt.imsave(fName + '/' + name, self.img)
            # cv2.imwrite(fName + '/' + name, self.img)
        except:
            print("Can't Save image")

