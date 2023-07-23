from PyQt5.QtWidgets import QApplication
import qdarkstyle
import sys
from home import Home
from login import Login
app = QApplication(sys.argv)
style = qdarkstyle.load_stylesheet(qt_api='pyqt5')
app.setStyleSheet(style)
style =style+ """
QPushButton {
    font: bold;
}  
"""
app.setStyleSheet(style)
home = Home()
login = Login(home)
app.exec_()


