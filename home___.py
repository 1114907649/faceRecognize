from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel,QVBoxLayout,QStackedWidget,QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QPainter
import numpy as np
import cv2
import time
from random import uniform
from PyQt5.Qt import *
from UI.Ui_form import Ui_Home  
from database import Database
import qdarkstyle


class Home(QtWidgets.QMainWindow,Ui_Home):
    def __init__(self) :
        super(Home,self).__init__()
        self.setupUi(self)
        self.init()
        #隐藏按钮
        self.hide_bt(False)
        #获取相机
        self.cap = cv2.VideoCapture(0)
        self.cap.release()
        #拍摄的图片
        self.Image = []
        #查看图片时的当前图片
        self.index = 0
        #实时图片
        self.showImage =None
        #创建数据库页面
        self.current_index.setStyleSheet("background-color: red")
        
    def init(self):
        # 定时器让其定时读取显示图片
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_image)
        # 打开摄像头
        self.open_bt.setVisible(True)
        self.open_bt.clicked.connect(self.open_camera)
        # 拍照
        self.photo_bt.clicked.connect(self.taking_pictures)
        # 关闭摄像头
        self.close_bt.clicked.connect(self.close_camera)

        #保存拍摄图片
        self.save_bt.clicked.connect(self.svae_image)
        #查看拍摄图片
        self.look_bt.clicked.connect(self.look_image)
        #删除拍摄的图片
        self.dele_bt.clicked.connect(self.delete_image)
        #上一张
        self.prev_bt.clicked.connect(self.prev_image)
        #下一张
        self.next_bt.clicked.connect(self.next_image)

        #导入图片
        #self.pushButton_5.clicked.connect(self.loadphoto)

    def hide_bt(self,T):
        self.dele_bt.setVisible(T)
        self.prev_bt.setVisible(T)
        self.next_bt.setVisible(T)
        self.save_bt.setVisible(not T)
        self.look_bt.setVisible(not T)
    '''开启摄像头'''
    def open_camera(self):
        self.hide_bt(False)
          # 摄像头
        self.cap = cv2.VideoCapture(0)
        self.camera_timer.start(40)  # 每40毫秒读取一次，即刷新率为25帧
        self.show_image()
    def prev_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index -1+len(self.Image))%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.image)))
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.Image[self.index]))
    def next_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index +1)%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.Image[self.index]))
    def delete_image(self):
        if(len(self.Image)>1):
            del self.Image[self.index]
            self.index  = (self.index -1)%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.image)))
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.Image[self.index]))
        elif(len(self.Image)>0) :
            del self.Image[self.index]
            self.label.clear()
    def svae_image(self):
        if self.showImage is not None:
            self.Image.append(self.showImage)
            self.camera_timer.start(40)
    def look_image(self):
        self.hide_bt(True)
        self.close_camera()
        if(len(self.Image)>0):
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.Image[self.index]))
    '''显示图片'''
    def show_image(self):
        flag, self.image = self.cap.read()  # 从视频流中读取图片
        #image_show = cv2.resize(self.image, (1280, 720))  # 把读到的帧的大小重新设置为 600*360
        image_show = self.image
        width, height = image_show.shape[:2]  # 行:宽，列:高
        image_show = cv2.cvtColor(image_show, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
        image_show = cv2.flip(image_show, 1)  # 水平翻转，因为摄像头拍的是镜像的。
        # 把读取到的视频数据变成QImage形式(图片数据、高、宽、RGB颜色空间，三个通道各有2**8=256种颜色)
        self.showImage = QtGui.QImage(image_show.data, height, width, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(self.showImage))  # 往显示视频的Label里显示QImage
        self.label.setScaledContents(True) #图片自适应
    '''拍照'''
    def taking_pictures(self):
        if self.cap.isOpened():
            self.camera_timer.stop()
            #FName = fr"images/cap{time.strftime('%Y%m%d%H%M%S', time.localtime())}"
            #print(FName)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.showImage))
            #self.showImage.save(FName + ".jpg", "JPG", 100)
            #self.showImage.save('./1.jpg')
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None

    '''开启摄像头'''
    def open_camera(self):
        if not self.cap.isOpened():
            self.hide_bt(False)
          # 摄像头
            self.cap = cv2.VideoCapture(0)
            self.camera_timer.start(40)  # 每40毫秒读取一次，即刷新率为25帧
            self.show_image()
    '''关闭摄像头'''
    def close_camera(self):
        self.camera_timer.stop()  # 停止读取
        self.cap.release()  # 释放摄像头
        self.label.clear()  # 清除label组件上的图片
        self.label.clear()  # 清除label组件上的图片
        # self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 摄像头
    #导入图片
    def loadphoto(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', '../', 'Image files(*.jpg *.gif *.png*.bmp)')
        self.showImage = fname
        self.label_2.setPixmap(QPixmap(self.showImage))
        
app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
home = Home()
home.show()
app.exec_()