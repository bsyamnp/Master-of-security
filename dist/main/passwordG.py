from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit
from random import randint as r
import pyperclip
import webbrowser

class Ui_MainWindow_gpw(object):
    def setupUi(self, MainWindow_gpw):
        chars = '@_$&#!/;<=>+-]{}[|~.,\%'
        def new_password():
                le = self.lineEdit.text()
                n = int(self.spinbox_length.value())
                if le !='':
                        password = ''
                        password = f'{password}{chars[r(0, len(chars) - 1)]}'
                        password = f'{password}{chars[r(0, len(chars) - 1)]}'
                        chars1 = le + chars
                        for i in le:
                                if i == 'a' or i=='A':
                                        password = f'{password}{chars[r(0, len(chars) - 1)]}'
                                if i == '0'or i=='O'or i=='o':
                                        password = f'{password}{chars[r(0, len(chars) - 1)]}'
                                else:
                                        password += i

                        for i in range(n-len(password)):
                                password = f'{password}{chars1[r(0, len(chars1) - 1)]}'
                        self.line_password.setText(password[0:n])
                else:
                        password = 'pw'
                        for i in range(n-len(password)):
                                password = f'{password}{chars[r(0, len(chars) - 1)]}'
                        self.line_password.setText(password[0:n])

        def change_password_visibility():
                if self.btn_visibility.isChecked():
                        self.line_password.setEchoMode(QLineEdit.Normal)
                else:
                        self.line_password.setEchoMode(QLineEdit.Password)

        def copy_to_clipboard() :
                pyperclip.copy(self.line_password.text())

        def regen():
                new_password()
        def open_web():
                webbrowser.open("https://www.actualidadgadget.com/kk/%D0%BA%D2%AF%D1%88%D1%82%D1%96-%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8C%D0%B4%D1%96-%D2%9B%D0%B0%D0%BB%D0%B0%D0%B9-%D0%B6%D0%B0%D1%81%D0%B0%D1%83%D2%93%D0%B0-%D0%B1%D0%BE%D0%BB%D0%B0%D0%B4%D1%8B/")
        MainWindow_gpw.setObjectName("MainWindow")
        MainWindow_gpw.resize(738, 521)
        MainWindow_gpw.setStyleSheet("background-color:rgb(246, 255, 255) ;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow_gpw)
        self.centralwidget.setObjectName("centralwidget")
        self.spinbox_length = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_length.setGeometry(QtCore.QRect(600, 350, 107, 62))
        self.spinbox_length.setStyleSheet("QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: rgb(164, 139, 227);\n"
"}\n"
"")
        self.spinbox_length.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinbox_length.setMinimum(10)
        self.spinbox_length.setMaximum(35)
        self.spinbox_length.setProperty("value", 12)
        self.spinbox_length.setObjectName("spinbox_length")
        self.slider_length = QtWidgets.QSlider(self.centralwidget)
        self.slider_length.setGeometry(QtCore.QRect(100, 360, 481, 42))
        self.slider_length.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slider_length.setStyleSheet("QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: rgb(164, 139, 227);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: rgb(151, 151, 181);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color:rgb(116, 59, 173);\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}\n"
"\n"
"")
        self.slider_length.setMinimum(10)
        self.slider_length.setMaximum(50)
        self.slider_length.setProperty("value", 12)
        self.slider_length.setOrientation(QtCore.Qt.Horizontal)
        self.slider_length.setObjectName("slider_length")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(480, 140, 241, 61))
        self.lineEdit.setStyleSheet("font: 63 12pt \"Bahnschrift SemiBold\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(0, 20, 81, 81))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 30, 311, 71))
        self.label_3.setStyleSheet("font: 13pt \"PMingLiU-ExtB\";\n"
"color: rgb(52, 0, 79);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 81, 521))
        self.label_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 140, 381, 61))
        self.label_7.setStyleSheet("background-color:rgb(213, 221, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold\";")
        self.label_7.setObjectName("label_7")
        self.frame_password = QtWidgets.QFrame(self.centralwidget)
        self.frame_password.setGeometry(QtCore.QRect(90, 240, 451, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setStyleSheet("QFrame {\n"
"    background-color: rgb(85, 85, 127);\n"
"    border: 2px solid rgb(215, 202, 255);\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: rgb(215, 202, 255);\n"
"}\n"
"\n"
"")
        self.frame_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_password.setObjectName("frame_password")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_password)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.line_password = QtWidgets.QLineEdit(self.frame_password)
        self.line_password.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}\n"
"")
        self.line_password.setObjectName("line_password")
        self.horizontalLayout_10.addWidget(self.line_password)
        self.btn_visibility = QtWidgets.QPushButton(self.frame_password)
        self.btn_visibility.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.btn_visibility.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("invisible.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("visible.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_visibility.setIcon(icon1)
        self.btn_visibility.setIconSize(QtCore.QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)
        self.btn_visibility.setObjectName("btn_visibility")
        self.horizontalLayout_10.addWidget(self.btn_visibility)
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy.setGeometry(QtCore.QRect(640, 240, 81, 81))
        self.btn_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet("QPushButton {\n"
"    background-color: rgb(85, 85, 127);\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"    border: 2px solid rgb(215, 202, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.btn_copy.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_copy.setIcon(icon2)
        self.btn_copy.setIconSize(QtCore.QSize(38, 38))
        self.btn_copy.setObjectName("btn_copy")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(560, 240, 71, 81))
        self.btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet("QPushButton {\n"
"    background-color: rgb(85, 85, 127);\n"
"    border: 2px solid rgb(215, 202, 255);\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}\n"
"\n"
"")
        self.btn_refresh.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QtCore.QSize(38, 38))
        self.btn_refresh.setObjectName("btn_refresh")
        self.pushButton_ppk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ppk.setGeometry(QtCore.QRect(400, 440, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_ppk.setFont(font)
        self.pushButton_ppk.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Bahnschrift SemiBold\";\n"
"border-radius: 10px;\n"
"background-color: rgb(117, 117, 175);\n"
"border-top-color: 3px transparent;\n"
"border-right-color: 3px transparent;\n"
"border-left-color: 3px transparent;\n"
"border-bottom-color: 3px transparent;\n"
"")
        self.pushButton_ppk.setObjectName("pushButton_ppk")
        self.spinbox_length.raise_()
        self.slider_length.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.pushButton_home.raise_()
        self.label_7.raise_()
        self.frame_password.raise_()
        self.btn_copy.raise_()
        self.btn_refresh.raise_()
        self.pushButton_ppk.raise_()
        MainWindow_gpw.setCentralWidget(self.centralwidget)
        self.lineEdit.textChanged.connect(new_password)
        self.btn_refresh.clicked.connect(regen)
        self.slider_length.valueChanged.connect(self.spinbox_length.setValue)
        self.spinbox_length.valueChanged.connect(self.slider_length.setValue)
        self.btn_visibility.clicked.connect(change_password_visibility)
        self.pushButton_ppk.clicked.connect(open_web)
        self.btn_copy.clicked.connect(copy_to_clipboard)
        self.spinbox_length.valueChanged.connect(new_password)
        self.retranslateUi(MainWindow_gpw)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_gpw)

    def retranslateUi(self, MainWindow_gpw):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_gpw.setWindowTitle(_translate("MainWindow_gpw", "Қауіпсіз құпиясөз ойлап табу"))
        self.label.setText(_translate("MainWindow_gpw", "Master of security"))
        self.label_3.setText(_translate("MainWindow_gpw", "- қауіпсіз құпиясөз ойлап табу"))
        self.label_7.setText(_translate("MainWindow_gpw", " Қолданылатын символдарды енгізіңіз:"))
        self.btn_copy.setShortcut(_translate("MainWindow_gpw", "Ctrl+C"))
        self.btn_refresh.setShortcut(_translate("MainWindow_gpw", "Ctrl+R"))
        self.pushButton_ppk.setText(_translate("MainWindow_gpw", "Құпиясөз туралы пайдалы кеңестер"))


