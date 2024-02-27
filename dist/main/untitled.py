from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def open_web():
                webbrowser.open("https://www.securitylab.ru/blog/personal/bezmaly/350620.php")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 521)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 738, 521))
        self.tabWidget.setStyleSheet("font: 75 9pt \"Comic Sans MS\";\n"
"color: rgb(224, 229, 255);\n"
"color: rgb(85, 0, 127);")
        self.tabWidget.setObjectName("tabWidget")
        self.bastapky_bet = QtWidgets.QWidget()
        self.bastapky_bet.setObjectName("bastapky_bet")
        self.label_6 = QtWidgets.QLabel(self.bastapky_bet)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Colonna MT\";")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.bastapky_bet)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 741, 331))
        self.label_5.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.bastapky_bet)
        self.label_7.setGeometry(QtCore.QRect(380, 20, 161, 31))
        self.label_7.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(230, 236, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.bastapky_bet)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 90, 221, 211))
        self.pushButton_11.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"")
        self.pushButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("free-icon-cyber-security-3518889.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QtCore.QSize(241, 221))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_paidaly = QtWidgets.QPushButton(self.bastapky_bet)
        self.pushButton_paidaly.setGeometry(QtCore.QRect(260, 400, 211, 71))
        self.pushButton_paidaly.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_paidaly.setObjectName("pushButton_paidaly")
        self.label_8 = QtWidgets.QLabel(self.bastapky_bet)
        self.label_8.setGeometry(QtCore.QRect(260, 80, 441, 261))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_aboutUs = QtWidgets.QPushButton(self.bastapky_bet)
        self.pushButton_aboutUs.setGeometry(QtCore.QRect(500, 400, 211, 71))
        self.pushButton_aboutUs.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_aboutUs.setObjectName("pushButton_aboutUs")
        self.pushButton_getService = QtWidgets.QPushButton(self.bastapky_bet)
        self.pushButton_getService.setGeometry(QtCore.QRect(20, 400, 211, 71))
        self.pushButton_getService.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getService.setObjectName("pushButton_getService")
        self.tabWidget.addTab(self.bastapky_bet, "")
        self.service_bet = QtWidgets.QWidget()
        self.service_bet.setObjectName("service_bet")
        self.pushButton_getBlockWeb = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_getBlockWeb.setGeometry(QtCore.QRect(270, 160, 161, 101))
        self.pushButton_getBlockWeb.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getBlockWeb.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("free-icon-web-lock-7146783.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getBlockWeb.setIcon(icon1)
        self.pushButton_getBlockWeb.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_getBlockWeb.setObjectName("pushButton_getBlockWeb")
        self.label = QtWidgets.QLabel(self.service_bet)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Colonna MT\";")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton_getGenerateP = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_getGenerateP.setGeometry(QtCore.QRect(270, 320, 161, 101))
        self.pushButton_getGenerateP.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getGenerateP.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-защита-в-реальном-времени-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getGenerateP.setIcon(icon2)
        self.pushButton_getGenerateP.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_getGenerateP.setObjectName("pushButton_getGenerateP")
        self.pushButton_getConv = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_getConv.setGeometry(QtCore.QRect(530, 320, 161, 101))
        self.pushButton_getConv.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getConv.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-главная-страница-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getConv.setIcon(icon3)
        self.pushButton_getConv.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_getConv.setObjectName("pushButton_getConv")
        self.pushButton_gethashDoc = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_gethashDoc.setGeometry(QtCore.QRect(530, 160, 161, 101))
        self.pushButton_gethashDoc.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_gethashDoc.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("free-icon-sha-256-5675076.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_gethashDoc.setIcon(icon4)
        self.pushButton_gethashDoc.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_gethashDoc.setObjectName("pushButton_gethashDoc")
        self.pushButton_getsteg = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_getsteg.setGeometry(QtCore.QRect(30, 320, 161, 101))
        self.pushButton_getsteg.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getsteg.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Verification-Badge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getsteg.setIcon(icon5)
        self.pushButton_getsteg.setIconSize(QtCore.QSize(150, 80))
        self.pushButton_getsteg.setObjectName("pushButton_getsteg")
        self.label_2 = QtWidgets.QLabel(self.service_bet)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 741, 381))
        self.label_2.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_getScan = QtWidgets.QPushButton(self.service_bet)
        self.pushButton_getScan.setGeometry(QtCore.QRect(30, 160, 161, 101))
        self.pushButton_getScan.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_getScan.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("prvkd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_getScan.setIcon(icon6)
        self.pushButton_getScan.setIconSize(QtCore.QSize(160, 100))
        self.pushButton_getScan.setObjectName("pushButton_getScan")
        self.label_3 = QtWidgets.QLabel(self.service_bet)
        self.label_3.setGeometry(QtCore.QRect(370, 40, 121, 31))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(230, 236, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.service_bet)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 151, 21))
        self.label_4.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.service_bet)
        self.label_9.setGeometry(QtCore.QRect(280, 260, 151, 21))
        self.label_9.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.service_bet)
        self.label_10.setGeometry(QtCore.QRect(530, 260, 171, 21))
        self.label_10.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.service_bet)
        self.label_11.setGeometry(QtCore.QRect(40, 420, 151, 21))
        self.label_11.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.service_bet)
        self.label_12.setGeometry(QtCore.QRect(280, 420, 151, 21))
        self.label_12.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.service_bet)
        self.label_13.setGeometry(QtCore.QRect(510, 420, 191, 21))
        self.label_13.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"color: rgb(70, 0, 106);\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.label_13.setObjectName("label_13")
        self.label_2.raise_()
        self.pushButton_getBlockWeb.raise_()
        self.label.raise_()
        self.pushButton_getGenerateP.raise_()
        self.pushButton_getConv.raise_()
        self.pushButton_gethashDoc.raise_()
        self.pushButton_getsteg.raise_()
        self.pushButton_getScan.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.tabWidget.addTab(self.service_bet, "")
        self.about_us = QtWidgets.QWidget()
        self.about_us.setObjectName("about_us")
        self.label_14 = QtWidgets.QLabel(self.about_us)
        self.label_14.setGeometry(QtCore.QRect(-10, 110, 741, 281))
        self.label_14.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.about_us)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Colonna MT\";")
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.about_us)
        self.label_16.setGeometry(QtCore.QRect(390, 40, 121, 31))
        self.label_16.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(230, 236, 255);")
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(self.about_us)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 171, 161))
        self.pushButton.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;")
        self.pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons8-информация-160.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QtCore.QSize(170, 180))
        self.pushButton.setObjectName("pushButton")
        self.label_17 = QtWidgets.QLabel(self.about_us)
        self.label_17.setGeometry(QtCore.QRect(270, 160, 401, 181))
        self.label_17.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.pushButton_paidaly_2 = QtWidgets.QPushButton(self.about_us)
        self.pushButton_paidaly_2.setGeometry(QtCore.QRect(260, 400, 211, 71))
        self.pushButton_paidaly_2.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_paidaly_2.setObjectName("pushButton_paidaly_2")
        self.pushButton_GService = QtWidgets.QPushButton(self.about_us)
        self.pushButton_GService.setGeometry(QtCore.QRect(20, 400, 211, 71))
        self.pushButton_GService.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_GService.setObjectName("pushButton_GService")
        self.pushButton_HomePage = QtWidgets.QPushButton(self.about_us)
        self.pushButton_HomePage.setGeometry(QtCore.QRect(500, 400, 211, 71))
        self.pushButton_HomePage.setStyleSheet("color: rgb(216, 217, 255);\n"
"background-color: rgb(43, 0, 65);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_HomePage.setObjectName("pushButton_HomePage")
        self.tabWidget.addTab(self.about_us, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_paidaly.clicked.connect(open_web)
        self.pushButton_paidaly_2.clicked.connect(open_web)
        self.pushButton_HomePage.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.pushButton_getService.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.pushButton_GService.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.pushButton_aboutUs.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.pushButton_getConv.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Master of security"))
        self.label_6.setText(_translate("MainWindow", "Master of security"))
        self.label_7.setText(_translate("MainWindow", "- бастапқы бет"))
        self.pushButton_paidaly.setText(_translate("MainWindow", "Пайдалы кеңестер"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Киберқауіпсіздік құпия деректерді, ақпаратты қорғауға қатысты барлық нәрсені қамтиды. Сол себепті бұл қосымша сізге келесі сервистерді ұсынады:</p><p>- Файлдарды тексеру</p><p>- Қауіпсіз құпиясөз құрау</p><p>- Документтерді хэштеу</p><p>- <span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Стеганография және т.б.</span></p></body></html>"))
        self.pushButton_aboutUs.setText(_translate("MainWindow", "Біз туралы"))
        self.pushButton_getService.setText(_translate("MainWindow", "Сервистер"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bastapky_bet), _translate("MainWindow", "Бастапқы бет"))
        self.label.setText(_translate("MainWindow", "Master of security"))
        self.label_3.setText(_translate("MainWindow", "- сервистер"))
        self.label_4.setText(_translate("MainWindow", "Файлды тексеру"))
        self.label_9.setText(_translate("MainWindow", "Сайтты блоктау"))
        self.label_10.setText(_translate("MainWindow", "Документті хэштеу"))
        self.label_11.setText(_translate("MainWindow", "Стеганография"))
        self.label_12.setText(_translate("MainWindow", "Қауіпсіз құпиясөз"))
        self.label_13.setText(_translate("MainWindow", "      Бастапқы бет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.service_bet), _translate("MainWindow", "Сервистер"))
        self.label_15.setText(_translate("MainWindow", "Master of security"))
        self.label_16.setText(_translate("MainWindow", "- біз туралы"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Master of security – киберқауіпсіздікті қамтамасыз етуге бағытталған қосымша. Біздің мақсатымыз технологиялар заманында қолданушылардың ақпараттық қауіпсіздігін қамтамасыз ету.</p></body></html>"))
        self.pushButton_paidaly_2.setText(_translate("MainWindow", "Пайдалы кеңестер"))
        self.pushButton_GService.setText(_translate("MainWindow", "Сервистер"))
        self.pushButton_HomePage.setText(_translate("MainWindow", "Бастапқы бет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_us), _translate("MainWindow", "Біз туралы"))




