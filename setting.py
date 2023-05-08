from PyQt5.QtWidgets import QWidget
from random import uniform
from UI.Ui_setting import Ui_form
class Setting(QWidget,Ui_form):
    def __init__(self,home) :
        super(Setting,self).__init__()
        self.setupUi(self)
        self.init()
        self.home =home
        self.home.stacked_widget.addWidget(self)
    def init(self):
        self.back_bt.clicked.connect(self.back_fc)
    def back_fc(self):
        self.home.stacked_widget.setCurrentWidget(self.home.screen)
