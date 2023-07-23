import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 Label 和 Button 组件
        self.label = QLabel('Hello World!', self)
        button = QPushButton('Click me', self)
        button.clicked.connect(self.show_label)

        # 创建垂直布局管理器并向其中添加组件
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(button)

        # 创建一个 QWidget 作为中心窗口部件，并将布局管理器应用于该 QWidget
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # 隐藏所有组件
        self.hide()

        # 设置窗口属性
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MyApp')

    def show_label(self):
        # 显示 Label 组件
        self.label.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()  # 显示窗口
    sys.exit(app.exec_())