from PyQt5.QtWidgets import QWidget,QLabel
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt
from random import uniform
from UI.Ui_login import Ui_form
class Login(QWidget,Ui_form):
    def __init__(self,home) :
        super(Login,self).__init__()
        self.setupUi(self)
        self.home  = home
        self.init()
        self.login.setVisible(False)
        self.resize(600,400)
        self.label = RoundLabel(self.label)
        pixmap = QPixmap('images/321/231/ng')
        self.label.setPixmap(pixmap)
        self.show()

    def init(self):
        self.password.returnPressed.connect(self.login_fc)
        self.password.textChanged.connect(self.message.clear)
        self.login.clicked.connect(self.login_fc)
        self.password.mousePressEvent=self.password.selectAll()
    def login_fc(self):
        if self.password.text() == '123456':
            self.home.show()
            self.hide()
        else :
            self.message.setText('密码错误')
class RoundLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)
        self.setScaledContents(True)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.rect())
        pixmap = self.pixmap()
        if not pixmap:
            return
        scaled_pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter.drawPixmap(self.rect(), scaled_pixmap)
