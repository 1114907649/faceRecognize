# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\imageViewOld.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(813, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QLabel { width: 50px; qproperty-alignment: AlignCenter; }\n"
"QPushButton { min-width: 80px;   }")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("QPushButton { min-width: 80px; }")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.horizontalLayout_8.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.department_box = QtWidgets.QComboBox(Form)
        self.department_box.setObjectName("department_box")
        self.department_box.addItem("")
        self.department_box.addItem("")
        self.horizontalLayout_12.addWidget(self.department_box)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.class_box = QtWidgets.QComboBox(Form)
        self.class_box.setObjectName("class_box")
        self.class_box.addItem("")
        self.class_box.addItem("")
        self.horizontalLayout_11.addWidget(self.class_box)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout_10.addWidget(self.name)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.ID = QtWidgets.QLineEdit(Form)
        self.ID.setObjectName("ID")
        self.horizontalLayout.addWidget(self.ID)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.update_bt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_bt.sizePolicy().hasHeightForWidth())
        self.update_bt.setSizePolicy(sizePolicy)
        self.update_bt.setObjectName("update_bt")
        self.horizontalLayout_13.addWidget(self.update_bt)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.delete_bt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_bt.sizePolicy().hasHeightForWidth())
        self.delete_bt.setSizePolicy(sizePolicy)
        self.delete_bt.setObjectName("delete_bt")
        self.horizontalLayout_5.addWidget(self.delete_bt)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.prev_bt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_bt.sizePolicy().hasHeightForWidth())
        self.prev_bt.setSizePolicy(sizePolicy)
        self.prev_bt.setObjectName("prev_bt")
        self.horizontalLayout_4.addWidget(self.prev_bt)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.next_bt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_bt.sizePolicy().hasHeightForWidth())
        self.next_bt.setSizePolicy(sizePolicy)
        self.next_bt.setObjectName("next_bt")
        self.horizontalLayout_3.addWidget(self.next_bt)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.setStretch(0, 8)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.back_bt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_bt.sizePolicy().hasHeightForWidth())
        self.back_bt.setSizePolicy(sizePolicy)
        self.back_bt.setObjectName("back_bt")
        self.horizontalLayout_6.addWidget(self.back_bt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "学院"))
        self.department_box.setItemText(0, _translate("Form", "计算机"))
        self.department_box.setItemText(1, _translate("Form", "外国语"))
        self.label_4.setText(_translate("Form", "班级"))
        self.class_box.setItemText(0, _translate("Form", "智科"))
        self.class_box.setItemText(1, _translate("Form", "数媒"))
        self.label_3.setText(_translate("Form", "姓名"))
        self.label_5.setText(_translate("Form", "学号"))
        self.update_bt.setText(_translate("Form", "修改"))
        self.delete_bt.setText(_translate("Form", "删除"))
        self.prev_bt.setText(_translate("Form", "上一张"))
        self.next_bt.setText(_translate("Form", "下一张"))
        self.back_bt.setText(_translate("Form", "返回"))
