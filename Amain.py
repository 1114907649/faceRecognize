from PyQt5.QtWidgets import QApplication
import qdarkstyle
import sys
from home import Home
from login import Login
app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
home = Home()
login = Login(home)
app.exec_()


