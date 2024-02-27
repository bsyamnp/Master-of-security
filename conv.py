from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from pdf2docx import parse
from docx2pdf import convert
class Ui_MainWindow_conv(object):
    def setupUi(self, MainWindow_conv):
        def open_file():
            filepath = filedialog.askopenfilename()
            with open(filepath, 'rb') as file:
                self.textEdit.setText(filepath)
                self.textEdit.setReadOnly(True)

        def convertword():
            try:
                pdf_file = self.textEdit.text()
                file_p, ff = pdf_file.split(".")
                word_file = file_p + '.docx'
                print(word_file)
                parse(pdf_file, word_file)
                self.label_7.setText("PDF файл word файылына ауысты")
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Critical)
                msgBox.setText("Error")
                msgBox.setInformativeText("Бұл файлдың форматын өзгертуге шек қойылған.")
                msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                msgBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                msgBox.exec_()


        def convertpdf():
            try:
                word_file = self.textEdit.text()
                file_p, ff = word_file.split(".")
                pdf_file = file_p + '.pdf'
                print(pdf_file)
                convert(word_file, pdf_file)
                self.label_7.setText("Word файл pdf файылына ауыстыру")
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Critical)
                msgBox.setText("Error")
                msgBox.setInformativeText("Бұл файлдың форматын өзгертуге шек қойылған.")
                msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                msgBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                msgBox.exec_()

        MainWindow_conv.setObjectName("MainWindow_conv")
        MainWindow_conv.resize(738, 521)
        MainWindow_conv.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_conv)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 151, 131))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("файл.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 100))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 131, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(320, 130, 371, 61))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 90, 371, 31))
        self.label_3.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 350, 111, 111))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("free-icon-pdf-174339.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 350, 111, 111))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("free-icon-word-888883.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 300, 171, 41))
        self.label_5.setStyleSheet("\n"
"font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 300, 181, 41))
        self.label_6.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 480, 431, 21))
        self.label_7.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(52, 0, 79);\n"
"font: 75 28pt \"Rockwell Condensed\";")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 0, 181, 71))
        self.label_4.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_4.setObjectName("label_4")
        self.pushButton_home_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home_3.setGeometry(QtCore.QRect(0, 40, 71, 81))
        self.pushButton_home_3.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-главная-страница-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home_3.setIcon(icon3)
        self.pushButton_home_3.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home_3.setObjectName("pushButton_home_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 71, 521))
        self.label_17.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 271, 671, 16))
        self.label_8.setStyleSheet("font: 63 6pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;\n"
"background-color: rgb(85, 85, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_17.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.pushButton_home_3.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        MainWindow_conv.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow_conv)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_conv)
        self.pushButton.clicked.connect(open_file)
        self.pushButton_3.clicked.connect(convertword)
        self.pushButton_2.clicked.connect(convertpdf)

    def retranslateUi(self, MainWindow_conv):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_conv.setWindowTitle(_translate("MainWindow_conv", "Файл форматын ауыстыру"))
        self.label_2.setText(_translate("MainWindow_conv", "<html><head/><body><p align=\"center\">Файл ашу</p></body></html>"))
        self.label_3.setText(_translate("MainWindow_conv", "Файлдың жолы"))
        self.label_5.setText(_translate("MainWindow_conv", "PDF - қа ауыстыру"))
        self.label_6.setText(_translate("MainWindow_conv", "Word - қа ауыстыру"))
        self.label_7.setText(_translate("MainWindow_conv", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow_conv", "Master of security"))
        self.label_4.setText(_translate("MainWindow_conv", "- конвертациялау"))


