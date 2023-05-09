import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 700)

        # 创建一个 QLabel
        self.label1 = QLabel(self)
        self.label1.setGeometry(50, 50, 400, 400)
        self.label1.setStyleSheet('background-color: yellow')

        # 在 label1 的区域 (50, 50, 100, 100) 放置另一个 QLabel
        self.label2 = QLabel(self.label1)
        self.label2.setGeometry(0, self.label1.height() -50, self.label1.width(), 50)
        self.label2.setStyleSheet('background-color: rgba(0, 0, 255, 50)')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())