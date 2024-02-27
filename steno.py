import os
from tkinter import filedialog
from stegano import lsb
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_steno(object):
    def setupUi(self, MainWindow_steno):
        def showimage():
                icon2 = QtGui.QIcon()
                icon2.addPixmap(
                        QtGui.QPixmap("C:\\Users\\marzh\\PycharmProjects\\sozh\\free-icon-images-7915428.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.encode_img.setIcon(icon2)
                self.encode_img.setIconSize(QtCore.QSize(100, 100))
                global filename
                filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=( ("PNG file", "*png"), ("JPG file", "*jpg"), ("All file", "*txt")))
                iconi = QtGui.QIcon()
                iconi.addPixmap(QtGui.QPixmap(filename),QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.encode_img.setIcon(iconi)
                self.encode_img.setIconSize(QtCore.QSize(180, 180))

        def showimage1():
                global filename1
                filename1 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                                       filetypes=(
                                                               ("PNG file", "*png"), ("JPG file", "*jpg"),
                                                               ("All file", "*txt")))

                iconi = QtGui.QIcon()
                iconi.addPixmap(QtGui.QPixmap(filename1),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.decode_img.setIcon(iconi)
                self.decode_img.setIconSize(QtCore.QSize(180, 180))

        def decode():
                if self.label_info_decode.text() != '':
                        secret = lsb.hide(filename1, self.label_info_decode.text())
                        fn, fmt = filename1.split(".")
                        steno_file = fn + "-steno." + fmt
                        secret.save(steno_file)
                        iconi = QtGui.QIcon()
                        iconi.addPixmap(QtGui.QPixmap(steno_file),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.result_img.setIcon(iconi)
                        self.result_img.setIconSize(QtCore.QSize(180, 180))
                        self.label_info_decode.clear()
                else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
                        msgBox.setText("Error")
                        msgBox.setInformativeText("Деректер енгізілмеген")
                        msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                        msgBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                        msgBox.exec_()
        def encode():
                result = lsb.reveal(filename)
                if result != '':
                        self.encode_result.setText(result)
                else:
                        self.encode_result.setText('Бұл файлда жасырылған сөздер жоқ!')
        def show_decode_page():
                self.stackedWidget.setCurrentIndex(2)
                icon2 = QtGui.QIcon()
                icon2.addPixmap(
                        QtGui.QPixmap("free-icon-images-7915428.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.decode_img.setIcon(icon2)
                self.decode_img.setIconSize(QtCore.QSize(100, 100))
                self.result_img.setIcon(icon2)
                self.result_img.setIconSize(QtCore.QSize(100, 100))
        def show_encode_page():
                self.stackedWidget.setCurrentIndex(1)
                icon2 = QtGui.QIcon()
                icon2.addPixmap(
                        QtGui.QPixmap("free-icon-images-7915428.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.encode_img.setIcon(icon2)
                self.encode_img.setIconSize(QtCore.QSize(100, 100))
                self.encode_result.clear()

        MainWindow_steno.setObjectName("MainWindow_steno")
        MainWindow_steno.resize(738, 521)
        MainWindow_steno.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_steno)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 738, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(100, 30, 291, 71))
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
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(390, 30, 251, 71))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 521))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_home = QtWidgets.QPushButton(self.page)
        self.pushButton_home.setGeometry(QtCore.QRect(0, 30, 71, 81))
        self.pushButton_home.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-главная-страница-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon)
        self.pushButton_home.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 120, 291, 231))
        self.pushButton_11.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width:2px;\n"
"border-color: rgb(85, 85, 127);\n"
"\n"
"")
        self.pushButton_11.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("steganography_cyberattacks.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(280, 280))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(80, 130, 331, 211))
        self.label_6.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"font: 75 10pt \"Comic Sans MS\";\n"
"color: rgb(63, 63, 95);\n"
"")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_encode = QtWidgets.QPushButton(self.page)
        self.pushButton_encode.setGeometry(QtCore.QRect(110, 400, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_encode.setFont(font)
        self.pushButton_encode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_encode.setObjectName("pushButton_encode")
        self.pushButton_decode = QtWidgets.QPushButton(self.page)
        self.pushButton_decode.setGeometry(QtCore.QRect(460, 400, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_decode.setFont(font)
        self.pushButton_decode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_decode.setObjectName("pushButton_decode")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.encode_result = QtWidgets.QLabel(self.page_2)
        self.encode_result.setGeometry(QtCore.QRect(370, 130, 321, 161))
        self.encode_result.setStyleSheet("border-color: rgb(85, 85, 127);\n"
" border-style: solid;\n"
"border-width: 1px;")
        self.encode_result.setText("")
        self.encode_result.setObjectName("encode_result")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(370, 80, 321, 41))
        self.label_7.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;")
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.pushButton_scan = QtWidgets.QPushButton(self.page_2)
        self.pushButton_scan.setGeometry(QtCore.QRect(80, 310, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_scan.setFont(font)
        self.pushButton_scan.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.pushButton_home_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_home_3.setGeometry(QtCore.QRect(0, 30, 71, 81))
        self.pushButton_home_3.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home_3.setText("")
        self.pushButton_home_3.setIcon(icon)
        self.pushButton_home_3.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home_3.setObjectName("pushButton_home_3")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 71, 521))
        self.label_17.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.encode_img = QtWidgets.QPushButton(self.page_2)
        self.encode_img.setGeometry(QtCore.QRect(80, 80, 281, 211))
        self.encode_img.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width:1px;\n"
"border-color: rgb(85, 85, 127);\n"
"\n"
"")
        self.encode_img.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("free-icon-images-7915428.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encode_img.setIcon(icon2)
        self.encode_img.setIconSize(QtCore.QSize(100, 100))
        self.encode_img.setObjectName("encode_img")
        self.pushButton_decode2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_decode2.setGeometry(QtCore.QRect(540, 480, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_decode2.setFont(font)
        self.pushButton_decode2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"background-color: rgb(117, 117, 175);\n"
"\n"
"")
        self.pushButton_decode2.setObjectName("pushButton_decode2")
        self.read_and_showresult = QtWidgets.QPushButton(self.page_2)
        self.read_and_showresult.setGeometry(QtCore.QRect(500, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.read_and_showresult.setFont(font)
        self.read_and_showresult.setStyleSheet("color: rgb(73, 73, 109);\n"
"font: 63 10pt \"Bahnschrift SemiBold\";\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"background-color: rgb(234, 226, 255);\n"
"border-color: rgb(103, 103, 154);\n"
"\n"
"\n"
"")
        self.read_and_showresult.setObjectName("read_and_showresult")
        self.encode_result.raise_()
        self.label_7.raise_()
        self.pushButton_scan.raise_()
        self.label_17.raise_()
        self.pushButton_home_3.raise_()
        self.encode_img.raise_()
        self.pushButton_decode2.raise_()
        self.read_and_showresult.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.decode_img = QtWidgets.QPushButton(self.page_5)
        self.decode_img.setGeometry(QtCore.QRect(90, 160, 291, 211))
        self.decode_img.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-color: rgb(85, 85, 127);\n"
"\n"
"")
        self.decode_img.setText("")
        self.decode_img.setIcon(icon2)
        self.decode_img.setIconSize(QtCore.QSize(100, 100))
        self.decode_img.setObjectName("decode_img")
        self.select_img = QtWidgets.QPushButton(self.page_5)
        self.select_img.setGeometry(QtCore.QRect(90, 380, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.select_img.setFont(font)
        self.select_img.setStyleSheet("color: rgb(73, 73, 109);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"background-color: rgb(234, 226, 255);\n"
"border-color: rgb(103, 103, 154);\n"
"")
        self.select_img.setObjectName("select_img")
        self.label_info_decode = QtWidgets.QLineEdit(self.page_5)
        self.label_info_decode.setGeometry(QtCore.QRect(90, 70, 611, 61))
        self.label_info_decode.setObjectName("label_info_decode")
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(90, 20, 291, 41))
        self.label_19.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";\n"
"border-radius: 5px;")
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.pushButton_home_4 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_home_4.setGeometry(QtCore.QRect(0, 30, 71, 81))
        self.pushButton_home_4.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home_4.setText("")
        self.pushButton_home_4.setIcon(icon)
        self.pushButton_home_4.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home_4.setObjectName("pushButton_home_4")
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 71, 521))
        self.label_21.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.save_result_img = QtWidgets.QPushButton(self.page_5)
        self.save_result_img.setGeometry(QtCore.QRect(450, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.save_result_img.setFont(font)
        self.save_result_img.setStyleSheet("color: rgb(73, 73, 109);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width:2px;\n"
"background-color: rgb(234, 226, 255);\n"
"border-color: rgb(103, 103, 154);\n"
"\n"
"\n"
"")
        self.save_result_img.setObjectName("save_result_img")
        self.result_img = QtWidgets.QPushButton(self.page_5)
        self.result_img.setGeometry(QtCore.QRect(410, 160, 291, 211))
        self.result_img.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-color: rgb(85, 85, 127);\n"
"\n"
"")
        self.result_img.setText("")
        self.result_img.setIcon(icon2)
        self.result_img.setIconSize(QtCore.QSize(100, 100))
        self.result_img.setObjectName("result_img")
        self.pushButton_encode2 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_encode2.setGeometry(QtCore.QRect(550, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_encode2.setFont(font)
        self.pushButton_encode2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_encode2.setObjectName("pushButton_encode2")
        self.decode_img.raise_()
        self.select_img.raise_()
        self.label_info_decode.raise_()
        self.label_19.raise_()
        self.label_21.raise_()
        self.pushButton_home_4.raise_()
        self.save_result_img.raise_()
        self.result_img.raise_()
        self.pushButton_encode2.raise_()
        self.stackedWidget.addWidget(self.page_5)
        MainWindow_steno.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow_steno)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_steno)
        self.pushButton_encode.clicked.connect(show_encode_page)
        self.pushButton_encode2.clicked.connect(show_encode_page)
        self.pushButton_scan.clicked.connect(showimage)
        self.select_img.clicked.connect(showimage1)
        self.pushButton_decode.clicked.connect(show_decode_page)
        self.pushButton_decode2.clicked.connect(show_decode_page)
        self.read_and_showresult.clicked.connect(encode)
        self.save_result_img.clicked.connect(decode)

    def retranslateUi(self, MainWindow_steno):
            _translate = QtCore.QCoreApplication.translate
            MainWindow_steno.setWindowTitle(_translate("MainWindow_steno", "Стеганография"))
            self.label.setText(_translate("MainWindow_steno", "Master of security"))
            self.label_3.setText(_translate("MainWindow_steno", "- стеганография "))
            self.label_6.setText(_translate("MainWindow_steno",
                                            "<html><head/><body><p align=\"center\">Стеганография – ақпаратты үшінші тұлғалар анықтай алмайтындай етіп жасыру әдісі. Криптографиядан айырмашылығы, стеганография мәліметтерді оқудан және өзгертуден қорғауға емес, олардың бар болу фактісін жасыруға бағытталған.</p></body></html>"))
            self.pushButton_encode.setText(_translate("MainWindow_steno", "Суреттен оқу"))
            self.pushButton_decode.setText(_translate("MainWindow_steno", "Суретке жазу"))
            self.label_7.setText(_translate("MainWindow_steno", " Жасырылған деректер:"))
            self.pushButton_scan.setText(_translate("MainWindow_steno", "Суретті таңдау"))
            self.pushButton_decode2.setText(_translate("MainWindow_steno", "Суретке жазу"))
            self.read_and_showresult.setText(_translate("MainWindow_steno", "Жасырын сөзді оқу"))
            self.select_img.setText(_translate("MainWindow_steno", "Суретті таңдау"))
            self.label_19.setText(_translate("MainWindow_steno", " Жасыру қажет деректер:"))
            self.save_result_img.setText(_translate("MainWindow_steno", "Жасыру және сақтау"))
            self.pushButton_encode2.setText(_translate("MainWindow_steno", "Суреттен оқу"))


