from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
import hashlib


class Ui_MainWindow_hash(object):
    def setupUi(self, MainWindow_hash):
        def open_file():
                filepath = filedialog.askopenfilename()
                self.textEdit.setText(filepath)
                with open(filepath, 'rb') as file:
                        md5 = hashlib.md5(filepath.encode())
                        sha1 = hashlib.sha1(filepath.encode())
                        sha224 = hashlib.sha224(filepath.encode())
                        sha256 = hashlib.sha256(filepath.encode())
                        sha384 = hashlib.sha384(filepath.encode())
                        sha512 = hashlib.sha512(filepath.encode())
                        a = ("md5: " + md5.hexdigest() + "\n") + ("sha1: " + sha1.hexdigest() + "\n") + (
                                        "sha224: " + sha224.hexdigest() + "\n") + (
                                            "sha256: " + sha256.hexdigest() + "\n") + (
                                            "sha384: " + sha384.hexdigest() + "\n") + (
                                            "sha512: " + sha512.hexdigest() + "\n")
                        self.label.setText(a)
        def clear():
            self.label.clear()
            self.textEdit.clear()
        MainWindow_hash.setObjectName("MainWindow_hash")
        MainWindow_hash.resize(738, 513)
        MainWindow_hash.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(255, 255, 255);")
        MainWindow_hash.setLocale(QtCore.QLocale(QtCore.QLocale.Kazakh, QtCore.QLocale.Kazakhstan))
        self.centralwidget = QtWidgets.QWidget(MainWindow_hash)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_home_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home_3.setGeometry(QtCore.QRect(0, 30, 71, 81))
        self.pushButton_home_3.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-главная-страница-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home_3.setIcon(icon)
        self.pushButton_home_3.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home_3.setObjectName("pushButton_home_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 71, 521))
        self.label_17.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 40, 251, 71))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(52, 0, 79);\n"
"font: 75 28pt \"Rockwell Condensed\";")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 151, 131))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("файл.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(160, 100))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 260, 131, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 180, 411, 61))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(53, 53, 80);")
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 140, 411, 31))
        self.label_5.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;\n"
"color: rgb(53, 53, 80);")
        self.label_5.setObjectName("label_5")
        self.pushButton_webClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_webClear.setGeometry(QtCore.QRect(470, 450, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_webClear.setFont(font)
        self.pushButton_webClear.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_webClear.setObjectName("pushButton_webClear")
        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 320, 591, 111))
        self.label.setStyleSheet("border-width:2px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 127);")
        self.label.setObjectName("label")
        self.label_17.raise_()
        self.pushButton_home_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label_5.raise_()
        self.pushButton_webClear.raise_()
        self.label.raise_()
        MainWindow_hash.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow_hash)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_hash)
        self.pushButton.clicked.connect(open_file)
        self.pushButton_webClear.clicked.connect(clear)

    def retranslateUi(self, MainWindow_hash):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_hash.setWindowTitle(_translate("MainWindow_hash", "Документті хэштеу"))
        self.label_3.setText(_translate("MainWindow_hash", "- документті хэштеу "))
        self.label_4.setText(_translate("MainWindow_hash", "Master of security"))
        self.label_2.setText(_translate("MainWindow_hash", "<html><head/><body><p align=\"center\">Файл ашу</p></body></html>"))
        self.label_5.setText(_translate("MainWindow_hash", "Файлдың жолы"))
        self.pushButton_webClear.setText(_translate("MainWindow_hash", "Тазарту"))
        self.label.setText(_translate("MainWindow_hash", ""))


