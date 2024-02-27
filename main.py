from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from scanfile1 import Ui_MainWindow_scan
from untitled import Ui_MainWindow
from webBlock import Ui_MainWindow_webBlocker
from hash import Ui_MainWindow_hash
from passwordG import Ui_MainWindow_gpw
from steno import Ui_MainWindow_steno

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def openScanPage():
    global MainWindow_scan
    MainWindow_scan = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_scan()
    ui.setupUi(MainWindow_scan)
    MainWindow.hide()
    MainWindow_scan.show()
    def homePage():
        MainWindow_scan.hide()
        MainWindow.show()
    ui.pushButton_home.clicked.connect(homePage)
    ui.pushButton_home_2.clicked.connect(homePage)
    

def hashPage():
    global MainWindow_hash
    MainWindow_hash = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_hash()
    ui.setupUi(MainWindow_hash)
    MainWindow.hide()
    MainWindow_hash.show()

    def homePage():
        MainWindow_hash.hide()
        MainWindow.show()
    ui.pushButton_home_3.clicked.connect(homePage)



def webBlockPage():
    global MainWindow_webBlocker
    MainWindow_webBlocker = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_webBlocker()
    ui.setupUi(MainWindow_webBlocker)
    MainWindow.hide()
    MainWindow_webBlocker.show()
    def homePage():
        MainWindow_webBlocker.hide()
        MainWindow.show()
    ui.pushButton_home.clicked.connect(homePage)
def open_gener_pw():
    MainWindow_gpw = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_gpw()
    ui.setupUi(MainWindow_gpw)
    MainWindow.hide()
    MainWindow_gpw.show()
    def homePage():
        MainWindow_gpw.hide()
        MainWindow.show()
    ui.pushButton_home.clicked.connect(homePage)
def open_steno_page():
    MainWindow_steno = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_steno()
    ui.setupUi(MainWindow_steno)
    MainWindow.hide()
    MainWindow_steno.show()
    def homePage():
        MainWindow_steno.hide()
        MainWindow.show()
    ui.pushButton_home.clicked.connect(homePage)
    ui.pushButton_home_3.clicked.connect(homePage)
    ui.pushButton_home_4.clicked.connect(homePage)


ui.pushButton_gethashDoc.clicked.connect(hashPage)
ui.pushButton_getScan.clicked.connect(openScanPage)
ui.pushButton_getBlockWeb.clicked.connect(webBlockPage)
ui.pushButton_getGenerateP.clicked.connect(open_gener_pw)
ui.pushButton_getsteg.clicked.connect(open_steno_page)
sys.exit(app.exec_())

