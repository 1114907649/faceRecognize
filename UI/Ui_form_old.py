# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\form_old.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(826, 615)
        self.screen = QtWidgets.QWidget(Home)
        self.screen.setObjectName("screen")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.screen)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top = QtWidgets.QHBoxLayout()
        self.top.setObjectName("top")
        self.titel = QtWidgets.QLabel(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titel.sizePolicy().hasHeightForWidth())
        self.titel.setSizePolicy(sizePolicy)
        self.titel.setObjectName("titel")
        self.top.addWidget(self.titel)
        self.verticalLayout_3.addLayout(self.top)
        self.mid = QtWidgets.QHBoxLayout()
        self.mid.setObjectName("mid")
        self.left = QtWidgets.QVBoxLayout()
        self.left.setObjectName("left")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.database = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.database.sizePolicy().hasHeightForWidth())
        self.database.setSizePolicy(sizePolicy)
        self.database.setMinimumSize(QtCore.QSize(80, 0))
        self.database.setBaseSize(QtCore.QSize(0, 0))
        self.database.setObjectName("database")
        self.horizontalLayout_2.addWidget(self.database)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.left.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.game = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game.sizePolicy().hasHeightForWidth())
        self.game.setSizePolicy(sizePolicy)
        self.game.setMinimumSize(QtCore.QSize(80, 0))
        self.game.setObjectName("game")
        self.horizontalLayout_3.addWidget(self.game)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.left.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.setting = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        self.setting.setMinimumSize(QtCore.QSize(80, 0))
        self.setting.setObjectName("setting")
        self.horizontalLayout_4.addWidget(self.setting)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.left.addLayout(self.horizontalLayout_4)
        self.mid.addLayout(self.left)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem7)
        self.current_index = QtWidgets.QLabel(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_index.sizePolicy().hasHeightForWidth())
        self.current_index.setSizePolicy(sizePolicy)
        self.current_index.setText("")
        self.current_index.setObjectName("current_index")
        self.horizontalLayout.addWidget(self.current_index)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.mid.addLayout(self.verticalLayout)
        self.right = QtWidgets.QVBoxLayout()
        self.right.setObjectName("right")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.department1 = QtWidgets.QLabel(self.screen)
        self.department1.setObjectName("department1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.department1)
        self.department = QtWidgets.QLineEdit(self.screen)
        self.department.setObjectName("department")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.department)
        self.classname1 = QtWidgets.QLabel(self.screen)
        self.classname1.setObjectName("classname1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.classname1)
        self.classname = QtWidgets.QLineEdit(self.screen)
        self.classname.setObjectName("classname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.classname)
        self.username1 = QtWidgets.QLabel(self.screen)
        self.username1.setObjectName("username1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.username1)
        self.username = QtWidgets.QLineEdit(self.screen)
        self.username.setObjectName("username")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username)
        self.ID1 = QtWidgets.QLabel(self.screen)
        self.ID1.setObjectName("ID1")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ID1)
        self.ID = QtWidgets.QLineEdit(self.screen)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.message = QtWidgets.QLabel(self.screen)
        self.message.setStyleSheet("color red;")
        self.message.setText("")
        self.message.setObjectName("message")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.message)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem8)
        self.right.addLayout(self.formLayout)
        self.save2 = QtWidgets.QPushButton(self.screen)
        self.save2.setObjectName("save2")
        self.right.addWidget(self.save2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.prev_bt = QtWidgets.QPushButton(self.screen)
        self.prev_bt.setObjectName("prev_bt")
        self.verticalLayout_5.addWidget(self.prev_bt)
        self.look_bt = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.look_bt.sizePolicy().hasHeightForWidth())
        self.look_bt.setSizePolicy(sizePolicy)
        self.look_bt.setObjectName("look_bt")
        self.verticalLayout_5.addWidget(self.look_bt)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.next_bt = QtWidgets.QPushButton(self.screen)
        self.next_bt.setObjectName("next_bt")
        self.verticalLayout_5.addWidget(self.next_bt)
        self.save_bt = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.save_bt.sizePolicy().hasHeightForWidth())
        self.save_bt.setSizePolicy(sizePolicy)
        self.save_bt.setObjectName("save_bt")
        self.verticalLayout_5.addWidget(self.save_bt)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.dele_bt = QtWidgets.QPushButton(self.screen)
        self.dele_bt.setObjectName("dele_bt")
        self.verticalLayout_5.addWidget(self.dele_bt)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.right.addLayout(self.verticalLayout_5)
        self.right.setStretch(0, 1)
        self.right.setStretch(2, 1)
        self.mid.addLayout(self.right)
        self.mid.setStretch(0, 1)
        self.mid.setStretch(1, 4)
        self.mid.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.mid)
        self.bottom = QtWidgets.QHBoxLayout()
        self.bottom.setSpacing(7)
        self.bottom.setObjectName("bottom")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom.addItem(spacerItem13)
        self.open_bt = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_bt.sizePolicy().hasHeightForWidth())
        self.open_bt.setSizePolicy(sizePolicy)
        self.open_bt.setObjectName("open_bt")
        self.bottom.addWidget(self.open_bt)
        self.photo_bt = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo_bt.sizePolicy().hasHeightForWidth())
        self.photo_bt.setSizePolicy(sizePolicy)
        self.photo_bt.setObjectName("photo_bt")
        self.bottom.addWidget(self.photo_bt)
        self.close_bt = QtWidgets.QPushButton(self.screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_bt.sizePolicy().hasHeightForWidth())
        self.close_bt.setSizePolicy(sizePolicy)
        self.close_bt.setIconSize(QtCore.QSize(20, 20))
        self.close_bt.setObjectName("close_bt")
        self.bottom.addWidget(self.close_bt)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom.addItem(spacerItem14)
        self.bottom.setStretch(0, 3)
        self.bottom.setStretch(4, 3)
        self.verticalLayout_3.addLayout(self.bottom)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 8)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        Home.setCentralWidget(self.screen)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menushezhi = QtWidgets.QMenu(self.menubar)
        self.menushezhi.setObjectName("menushezhi")
        Home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Home)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Home)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menushezhi.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menushezhi.menuAction())

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.titel.setText(_translate("Home", "只鹦"))
        self.database.setText(_translate("Home", "数据库"))
        self.game.setText(_translate("Home", "游戏"))
        self.setting.setText(_translate("Home", "设置"))
        self.department1.setText(_translate("Home", "学院"))
        self.classname1.setText(_translate("Home", "班级"))
        self.username1.setText(_translate("Home", "姓名"))
        self.ID1.setText(_translate("Home", "学号"))
        self.save2.setText(_translate("Home", "录入"))
        self.prev_bt.setText(_translate("Home", "上一张"))
        self.look_bt.setText(_translate("Home", "查看照片"))
        self.next_bt.setText(_translate("Home", "下一张"))
        self.save_bt.setText(_translate("Home", "保存"))
        self.dele_bt.setText(_translate("Home", "删除"))
        self.open_bt.setText(_translate("Home", "打开摄像头"))
        self.photo_bt.setText(_translate("Home", "拍照"))
        self.close_bt.setText(_translate("Home", "关闭摄像头"))
        self.menu.setTitle(_translate("Home", "文件"))
        self.menushezhi.setTitle(_translate("Home", "设置"))
        self.action.setText(_translate("Home", "导入"))
        self.action_2.setText(_translate("Home", "修改密码"))
