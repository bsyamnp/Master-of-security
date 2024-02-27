from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_webBlocker(object):
    def setupUi(self, MainWindow_webBlocker):
        def clear():
            self.lineEdit.clear()
        host_path = 'C:\Windows\System32\drivers\etc\hosts'
        ip_address = '127.0.0.1'
        def Blocker():
            Website = self.lineEdit.text()
            with open(host_path, 'r+') as host_file:
                file_content = host_file.read()
                print(file_content)
                if Website in file_content:
                    self.label_webState.setText(('Бұл бұғатталған сайт'))
                    pass
                else:
                    host_file.write(ip_address + " " + Website + '\n')
                    self.label_webState.setText(("Бұғатталды"))
                    
        MainWindow_webBlocker.setObjectName("MainWindow_webBlocker")
        MainWindow_webBlocker.resize(738, 521)
        MainWindow_webBlocker.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_webBlocker)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 81, 521))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 60, 251, 71))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 291, 71))
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 160, 581, 61))
        self.label_7.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_7.setObjectName("label_7")
        self.label_webState = QtWidgets.QLabel(self.centralwidget)
        self.label_webState.setGeometry(QtCore.QRect(90, 410, 581, 81))
        self.label_webState.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_webState.setText("")
        self.label_webState.setObjectName("label_webState")
        self.pushButton_blockWeb = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_blockWeb.setGeometry(QtCore.QRect(440, 340, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_blockWeb.setFont(font)
        self.pushButton_blockWeb.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_blockWeb.setObjectName("pushButton_blockWeb")
        self.pushButton_webClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_webClear.setGeometry(QtCore.QRect(90, 340, 231, 61))
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
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(0, 30, 81, 81))
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 240, 581, 91))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow_webBlocker.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_webBlocker)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_webBlocker)
        self.pushButton_blockWeb.clicked.connect(Blocker)
        self.pushButton_webClear.clicked.connect(clear)

    def retranslateUi(self, MainWindow_webBlocker):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_webBlocker.setWindowTitle(_translate("MainWindow_webBlocker", "Веб сайтты блоктау"))
        self.label_3.setText(_translate("MainWindow_webBlocker", "- веб сайтқа құлып қою"))
        self.label.setText(_translate("MainWindow_webBlocker", "Master of security"))
        self.label_7.setText(_translate("MainWindow_webBlocker", "Веб сайтты енгізіңіз:"))
        self.pushButton_blockWeb.setText(_translate("MainWindow_webBlocker", "Құлыптау"))
        self.pushButton_webClear.setText(_translate("MainWindow_webBlocker", "Тазарту"))
        



