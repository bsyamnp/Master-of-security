from PyQt5 import QtCore, QtGui, QtWidgets
import configparser
import hashlib
import os

osy_dir= os.path.dirname(__file__)

settings_file_path = osy_dir + '/settings/settings.ini'

config = configparser.ConfigParser()
config.read(settings_file_path)

SHA256_HASHES_pack1 = (osy_dir + '\\hard_signatures\\SHA256-Hashes_pack1.txt')
SHA256_HASHES_pack2 = (osy_dir + '\\hard_signatures\\SHA256-Hashes_pack2.txt')
SHA256_HASHES_pack3 = (osy_dir + '\\hard_signatures\\SHA256-Hashes_pack3.txt')

VERSION = "2.5"
DEV = "cookie0_o, Len-Stevens"


def FaildyJoiy(file):
    try:
        os.remove(file)
    except:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setText("Error")
        msgBox.setInformativeText(f"""\
Файлды жою мүмкін емес.
File: {file}"
            """)
        msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msgBox.exec_()
    finally:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Info")
        msgBox.setInformativeText(f"""\
Файл сәтті жойылды.
File: {file}"
            """)
        msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msgBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msgBox.exec_()

def NatijeDisplayVirusBar(self, file):
    self.Tabs.setCurrentIndex(1)
    self.label_9.setText("БАР!")
    self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(172, 40, 40);\n"
                                       "font: 63 12pt 'Bahnschrift SemiBold';""")
    self.pushButton_DeleteFile.clicked.connect(lambda: FaildyJoiy(file))
    self.pushButton_GetscanPage.clicked.connect(lambda: self.Tabs.setCurrentIndex(0))


def NatijeDisplayVirusJok(self, file):
    self.Tabs.setCurrentIndex(1)
    self.label_9.setText("ЖОҚ:)")
    self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
                               "background-color: rgb(170, 255, 127);\n"
                               "font: 63 12pt 'Bahnschrift SemiBold';""")
    self.pushButton_DeleteFile.clicked.connect(lambda: FaildyJoiy(file))
    self.pushButton_GetscanPage.clicked.connect(lambda: self.Tabs.setCurrentIndex(0))

def FileScanerleu(file, self, MainWindow):
        virus_bar = False
        with open(file, "rb") as f:
            bytetar = f.read()
            fileHashy = hashlib.sha256(bytetar).hexdigest();
        self.label_8.setText("File Hash:  " + fileHashy)

        with open(SHA256_HASHES_pack1, 'r') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                if str(fileHashy) == str(line.split(";")[0]):
                    virus_bar = True
                    f.close()
        f.close()
        if virus_bar == True:
            pass
        else:
            pass
        if virus_bar == False:
            with open(SHA256_HASHES_pack2, 'r') as f:
                lines = [line.rstrip() for line in f]
                for line in lines:
                    if str(fileHashy) == str(line.split(";")[0]):
                        virus_bar = True
                        f.close()
            f.close()
        else:
            pass
        if virus_bar == False:
            with open(SHA256_HASHES_pack3, 'r') as f:
                lines = [line.rstrip() for line in f]
                for line in lines:
                    if str(fileHashy) == str(line.split(";")[0]):
                        virus_bar = True
                        f.close()
            f.close()
        else:
            pass

        if virus_bar==True:
            NatijeDisplayVirusBar(self, file)
            self.Tabs.setCurrentIndex(1)

        else:
            NatijeDisplayVirusJok(self,file)
            self.Tabs.setCurrentIndex(1)
        return

def FileTandau(MainWindow, self):
    filepath_raw, filename_raw = os.path.split(str(QtWidgets.QFileDialog.getOpenFileName(MainWindow,
                                                                    "Select File",
                                                                    "YOUR-FILE-PATH")))
    filepath_raw = filepath_raw.replace("('", "")
    filename = filename_raw.replace("', 'All Files (*)')", "")
    self.label_fileName.setText("File Name: " + filename)
    filepath = (filepath_raw + "/" + filename)
    self.label_MestoFile.setText("File Path:  " + filepath)
    if(filepath_raw!=""):
        FileScanerleu(filepath, self, MainWindow)

class Ui_MainWindow_scan(object):
    def setupUi(self, MainWindow_scan):
        MainWindow_scan.setObjectName("MainWindow_scan")
        MainWindow_scan.resize(745, 521)
        MainWindow_scan.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_scan)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QStackedWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 736, 530))
        self.Tabs.setObjectName("Tabs")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 91, 521))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_scan = QtWidgets.QPushButton(self.page)
        self.pushButton_scan.setGeometry(QtCore.QRect(490, 300, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_scan.setFont(font)
        self.pushButton_scan.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(120, 180, 341, 191))
        self.label_4.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"font: 75 10pt \"Comic Sans MS\";\n"
"color: rgb(63, 63, 95);\n"
"")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(400, 70, 251, 71))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_3.setObjectName("label_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(480, 180, 251, 111))
        self.pushButton_11.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"")
        self.pushButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Снимок экрана 2022-12-04 162800.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_home = QtWidgets.QPushButton(self.page)
        self.pushButton_home.setGeometry(QtCore.QRect(0, 30, 91, 91))
        self.pushButton_home.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-главная-страница-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home.setObjectName("pushButton_home")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(110, 70, 291, 71))
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
        self.Tabs.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_GetscanPage = QtWidgets.QPushButton(self.page_2)
        self.pushButton_GetscanPage.setEnabled(True)
        self.pushButton_GetscanPage.setGeometry(QtCore.QRect(100, 410, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_GetscanPage.setFont(font)
        self.pushButton_GetscanPage.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_GetscanPage.setObjectName("pushButton_GetscanPage")
        self.pushButton_DeleteFile = QtWidgets.QPushButton(self.page_2)
        self.pushButton_DeleteFile.setEnabled(True)
        self.pushButton_DeleteFile.setGeometry(QtCore.QRect(410, 410, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_DeleteFile.setFont(font)
        self.pushButton_DeleteFile.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_DeleteFile.setObjectName("pushButton_DeleteFile")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 81, 521))
        self.label_5.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(410, 40, 251, 71))
        self.label_10.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_10.setObjectName("label_10")
        self.label_MestoFile = QtWidgets.QLabel(self.page_2)
        self.label_MestoFile.setEnabled(True)
        self.label_MestoFile.setGeometry(QtCore.QRect(110, 180, 541, 41))
        self.label_MestoFile.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_MestoFile.setText("")
        self.label_MestoFile.setObjectName("label_MestoFile")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(380, 300, 271, 61))
        self.label_9.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(110, 40, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(52, 0, 79);\n"
"font: 75 28pt \"Rockwell Condensed\";")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_fileName = QtWidgets.QLabel(self.page_2)
        self.label_fileName.setEnabled(True)
        self.label_fileName.setGeometry(QtCore.QRect(110, 120, 541, 41))
        self.label_fileName.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_fileName.setText("")
        self.label_fileName.setObjectName("label_fileName")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(110, 300, 251, 61))
        self.label_7.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_7.setObjectName("label_7")
        self.pushButton_home_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_home_2.setEnabled(True)
        self.pushButton_home_2.setGeometry(QtCore.QRect(0, 20, 81, 81))
        self.pushButton_home_2.setStyleSheet("background-color: rgb(246, 255, 255);\n"
"border-color: rgb(75, 73, 127);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(177, 158, 235);")
        self.pushButton_home_2.setText("")
        self.pushButton_home_2.setIcon(icon1)
        self.pushButton_home_2.setIconSize(QtCore.QSize(120, 100))
        self.pushButton_home_2.setObjectName("pushButton_home_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(110, 240, 541, 41))
        self.label_8.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.Tabs.addWidget(self.page_2)
        MainWindow_scan.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_scan)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_scan)
        self.pushButton_scan.clicked.connect(lambda: FileTandau(MainWindow_scan, self))

    def retranslateUi(self, MainWindow_scan):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_scan.setWindowTitle(_translate("MainWindow_scan", "Файлды сканерлеу"))
        self.pushButton_scan.setText(_translate("MainWindow_scan", "Файлды сканерлеу"))
        self.label_4.setText(_translate("MainWindow_scan", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Таңдалған файлдарды сканерлеуге және вирус жұққан деп тапқан файлдарды жоюға қабілетті қосымшаның сервисі. Мұнда инфекцияларды анықтау үшін MD5, SHA1 және SHA256 зиянды бағдарлама хэштерінің үлкен тізімін пайдаланады.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow_scan", "- файлды тексеру"))
        self.label.setText(_translate("MainWindow_scan", "Master of security"))
        self.pushButton_GetscanPage.setText(_translate("MainWindow_scan", "Қайталау"))
        self.pushButton_DeleteFile.setText(_translate("MainWindow_scan", "Файлды жою"))
        self.label_10.setText(_translate("MainWindow_scan", "- нәтиже"))
        self.label_6.setText(_translate("MainWindow_scan", "Master of security"))
        self.label_7.setText(_translate("MainWindow_scan", "Бұл файлда вирустар:"))



