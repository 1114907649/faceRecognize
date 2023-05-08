import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel,QVBoxLayout,QStackedWidget,QWidget,QFormLayout,QDesktopWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtSql import QSqlQuery
import numpy as np
import cv2
from recognition import Recognize
from retinaface_detect_align_module import retinaface_dnn
import time
from random import uniform
from PyQt5.QtCore import Qt
from DB.UserDB import userDB
from UI.Ui_form import Ui_Home  
from database import Database
from UI import game
import sys
import qdarkstyle
from PyQt5 import QtWidgets
#import qtvscodestyle as qtvsc
from login import Login
from setting import Setting
import pickle
class MyMainWindowWidget(QWidget):
    def __init__(self,main_window ):
        super().__init__()
        self.main_window = main_window 
        layout = QVBoxLayout()
        layout.addWidget(self.main_window)
        self.setLayout(layout)
        self.show()
class Home(QtWidgets.QMainWindow,Ui_Home):
    def __init__(self) :
        super(Home,self).__init__()
        self.setupUi(self)
        
        self.init()
        self.isclicklook = False
        #获取相机
        self.cap = cv2.VideoCapture(0)
        self.cap.release()
        #拍摄的图片
        self.Image = []
        #查看图片时的当前图片下标
        self.index = 0
        #实时图片
        self.showImage =None
        #创建数据库页面
        self.stacked_widget = QStackedWidget()
        self.databaseWindow =  Database(self) 
        #隐藏按钮
        self.hide_bt(False)
        self.hide_save_bt(False)
        #创建设置页面
        self.settingWindow = Setting(self)
        self.stacked_widget.addWidget(self.screen)
        
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.screen)
        self.stacked_widget.currentWidget().Image =  []
        #self.windowSize = QDesktopWidget().screenGeometry(self)
        #w = self.windowSize.width()
        #h = self.windowSize.height()
        self.resize(1100+200,750)
        self.restore = False
        self.recogniser = Recognize()
        self.detector = retinaface_dnn(align=True)
        self.face = None
    def init(self):
        # 定时器让其定时读取显示图片
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_image)
        # 打开摄像头
        self.open_bt.clicked.connect(self.open_camera)
        # 拍照
        self.photo_bt.clicked.connect(self.taking_pictures)
        # 关闭摄像头
        self.close_bt.clicked.connect(self.close_camera)
        #保存当前显示图片
        self.save_bt.clicked.connect(self.svae_image)
        #保存拍摄图片
        self.look_bt.clicked.connect(self.look_image)
        #开始游戏
        self.game.clicked.connect(game.start)
        #查看拍摄图片
        self.dele_bt.clicked.connect(self.delete_image)
        #上一张
        self.prev_bt.clicked.connect(self.prev_image)
        #下一张
        self.next_bt.clicked.connect(self.next_image)

        #打开数据库页面
        self.database.clicked.connect(self.hide_home)
        #打开设置页面
        self.setting.clicked.connect(self.setting_fc)
        #导入图片
        self.load_images.triggered.connect(self.load_images_fc)
        
        #将信息输入数据库
        self.save2.clicked.connect(self.store_image)
        self.resave2.accepted.connect(self.accept_fc)
        
        self.resave2.rejected.connect(self.reject_fc)
    def accept_fc(self):
        self.restore =True
        self.store_image()
    def reject_fc(self):
        self.restore =False
        self.store_image()
        self.hide_save_bt(False)
    def setting_fc(self):
        self.isclicklook = False
        self.current_index.clear()
        self.stacked_widget.setCurrentWidget(self.settingWindow)
    def store_image(self):
        department = self.department.text()
        classname  = self.classname.text()
        username   = self.username.text()
        ID         = self.ID.text()
        save_path = './images/'+department+'/'+classname+'/'+ID+ '_'+username
        if department and classname and username and ID:
            query = QSqlQuery()
            query.exec_("SELECT * FROM user_table WHERE ID = '%s'" % ID)
            if query.next():
                self.message.setText('该用户已存在,是否进行覆盖')
                if not self.restore:
                    self.hide_save_bt(True)
                    return
                else :
                    query.exec_("DELETE FROM user_table WHERE ID = '%s'" % ID)
                    self.restore = False   
                    self.hide_save_bt(False)
            
            images_path = save_path+'/'
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            for i in range(len(self.Image)):
                images_path  =images_path+','+'%d.png'%(i+1)
                self.Image[i].save(save_path+'/'+'%d.png'%(i+1))
            query = QSqlQuery()
            query.exec_("INSERT INTO user_table VALUES ('%s', '%s', '%s', '%s','%s')"%(department,classname,username,ID,images_path))
            self.recogniser.save_feat(ID,self.face)
            #self.databaseWindow.db = userDB()
            #self.databaseWindow.tableView.setModel(self.databaseWindow.db.model)
            self.databaseWindow.conbox_init()
            self.databaseWindow.db.model.select()
            self.message.setText('录入成功')
            self.clearAll()
        else :
            self.message.setText('请输入完整信息')
    def clearAll(self):
        self.label.clear()
        self.Image = []
        self.index = 0
        self.department.clear()
        self.classname.clear()
        self.ID.clear()
        self.username.clear()
        self.current_index.clear()
        
    def hide_home(self):
        self.isclicklook = False
        self.current_index.clear()
        self.stacked_widget.setCurrentWidget(self.databaseWindow)
    def hide_bt(self,T):
        self.dele_bt.setVisible(T)
        self.prev_bt.setVisible(T)
        self.next_bt.setVisible(T)
        self.save_bt.setVisible(not T)
        self.look_bt.setVisible(not T)
    def hide_save_bt(self,T):
        self.resave2.setVisible(T)
        self.save2.setVisible(not T)
    '''开启摄像头'''

    def prev_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index -1+len(self.Image))%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            self.show_save_image()
    def next_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index +1)%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            self.show_save_image()
    def delete_image(self):
        if(len(self.Image)>1):
            del self.Image[self.index]
            self.index  = (self.index -1)%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            self.show_save_image()
        elif(len(self.Image)>0) :
            del self.Image[self.index]
            self.label.clear()
            self.current_index.clear()
    def svae_image(self):
        if self.showImage is not None:
            self.Image.append(self.showImage)
            self.camera_timer.start(40)
    def look_image(self):
        self.isclicklook = True
        self.hide_bt(True)
        self.close_camera()
        if(len(self.Image)>0):
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            
            #self.label.setPixmap((self.Image[self.index]))
            self.show_save_image()
    '''显示图片'''
    def show_save_image(self):
        scaled_pixmap = self.Image[self.index].scaled(self.label.width()-7,self.label.height()-7, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
    def show_image(self):
        flag, self.image = self.cap.read()  # 从视频流中读取图片
        image_show = self.image
        drawing, face_rois = self.detector.detect(image_show)
        if len(face_rois) != 0:
            image_show = drawing
            query = QSqlQuery()
            for face in face_rois:
                face_id = self.recogniser.face_match(face)
                self.face = face 
                query.exec_("SELECT * FROM user_table WHERE ID = '%s'" %face_id)
                if query.first():
                    username = query.value(2)
                    id =  query.value(3)
                    self.current_index.setStyleSheet("background-color: green")
                    self.current_index.setText(f'{id}{username}')
                else:
                    self.current_index.setStyleSheet("background-color: red")
                    self.current_index.setText('陌生人')
                print(face_id)
        else:
            self.current_index.setStyleSheet("background-color: transparent")
            self.current_index.clear()
                
            
        width, height = image_show.shape[:2]  # 行:宽，列:高
        image_show = cv2.cvtColor(image_show, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
        image_show = cv2.flip(image_show, 1)  # 水平翻转，因为摄像头拍的是镜像的。
        # 把读取到的视频数据变成QImage形式(图片数据、高、宽、RGB颜色空间，三个通道各有2**8=256种颜色)
        #self.label.setScaledContents(True) 
        pixmap = QPixmap.fromImage(QtGui.QImage(image_show.data, height, width, QImage.Format_RGB888))
        scaled_pixmap = pixmap.scaled(self.label.width()-7,self.label.height()-7, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        
        
        self.showImage = pixmap
        #scaled_pixmap = pixmap.scaledToWidth(self.label.width(), Qt.SmoothTransformation)
        #self.label.setScaledContents(True) 
        """
        pass
        """
          # 往显示视频的Label里显示QImage
        #self.label.resize(self.frame.width()-2, self.frame.height()-2)
        #图片自适应
    '''拍照'''
    def taking_pictures(self):
        if self.cap.isOpened():
            self.camera_timer.stop()
            self.label.setPixmap((self.showImage))
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None
    '''开启摄像头'''
    def open_camera(self):
        if not self.cap.isOpened():
            self.isclicklook = False
            self.current_index.clear()
            self.hide_bt(False)
          # 摄像头
            self.cap = cv2.VideoCapture(0)
            self.camera_timer.start(20)  # 每40毫秒读取一次，即刷新率为25帧
            self.show_image()
    '''关闭摄像头'''
    def close_camera(self):
        
        self.camera_timer.stop()  # 停止读取
        self.cap.release()  # 释放摄像头
        self.label.clear()  # 清除label组件上的图片
        self.label.clear()  # 清除label组件上的图片
    #导入图片
    def load_images_fc(self):
        # 打开文件夹并选择多个图片
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilters(["Images (*.png *.xpm *.jpg)"])
        if file_dialog.exec_():
            # 获取所选文件的路径并添加到self.Image列表中
            file_names = file_dialog.selectedFiles()
            current_widget = self.stacked_widget.currentWidget()
            current_widget.store_image()
            n = len(self.Image)
            for file_name in file_names:
                pixmap = QPixmap(file_name)
                current_widget.Image.append(pixmap)
            current_widget.store_new_image(n)
            current_widget.show_save_image()
        
            if current_widget ==self.screen:
                self.Image = current_widget.Image
    def resizeEvent(self, event):
        # 在这里调用您想要执行的函数
        if not self.cap.isOpened() and self.isclicklook:
            self.show_save_image()
        super().resizeEvent(event)
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    home = Home()
    home.show()
    app.exec_()
