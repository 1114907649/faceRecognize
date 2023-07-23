import os
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel,QVBoxLayout,QStackedWidget,QWidget,QFormLayout,QDesktopWidget
from PyQt5.QtCore import QTimer,QThread
from PyQt5.QtGui import QImage, QPixmap,QFont,QPainterPath

from PyQt5.QtWidgets import QMessageBox,QCompleter
from PyQt5.QtGui import QPixmap, QPainter,QColor
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
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
import mysql.connector


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
        self.Face = []
        #查看图片时的当前图片下标
        self.index = 0
        #实时图片
        
        self.showImage =None
        #创建数据库页面
        self.stacked_widget = QStackedWidget()
        self.databaseWindow =  Database(self) 

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
        self.label2 = CropQLabel(self.label)
        font = QFont()
        font.setBold(True)
        font.setPointSize(self.label.height()//10)
        self.label2.setFont(font)
        self.circ = QLabel(self.label2)
        self.label2.setStyleSheet("background-color: transparent")
        self.inticompleter()
        self.threadRun = True
        #隐藏按钮
        self.hide_bt(False)
        self.hide_save_bt(False)
        self.initMysql()
    def init(self):
        # 定时器让其定时读取显示图片
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_image)

        


        self.department.editingFinished.connect(self.departmentChange)
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
            self.initMysql()
            self.message.setText('录入成功')
            self.clearAll()
        else :
            self.message.setText('请输入完整信息')
    def clearAll(self):
        self.label.clear()
        self.Image = []
        self.index = 0
        #self.department.clear()
        #self.classname.clear()
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
        self.label2.setVisible(not T)
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
            self.Face.append(self.face)
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

        width, height = self.image.shape[:2]  # 行:宽，列:高
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # opencv读的通道是BGR,要转成RGB
        self.image = cv2.flip(self.image, 1)  # 水平翻转，因为摄像头拍的是镜像的。
        

        
        
        self.pixmap = QPixmap.fromImage(QtGui.QImage(self.image.data, height, width, QImage.Format_RGB888))
        scaled_pixmap = self.pixmap.scaled(self.label.width()-7,self.label.height()-7, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.showImage = scaled_pixmap
        
        self.label.setPixmap(scaled_pixmap)



            

    def Reco(self):

        drawing, face_rois = self.detector.detect(self.image)
        if len(face_rois) != 0:
            self.label2.setVisible(True)
            self.label2.setGeometry(self.label.height()//20, self.label.height() -self.label.height()//7 -self.label.height()//30, self.label.width()-self.label.height()//10, self.label.height()//7)
            self.label2.setRadius(self.label.height()//14)
            self.circ.setGeometry(0,0,self.label.height()//7,self.label.height()//7)
            cir  =self.cirCrop(self.pixmap,self.label.height()//7)

            

            for face in face_rois:
                
                face_id = self.recogniser.face_match(face)
                self.face = face


                # 创建游标对象
                query = self.mydb.cursor()
                query.execute("SELECT * FROM user_table WHERE ID = '%s'" % face_id)
                result = query.fetchone()
                if result:
                    username = result[2]
                    id =  result[3]
                    self.label2.setColor(QColor(0, 0, 255, 100))
                    self.label2.setText(f'{id}{username}')
                    self.circ.setPixmap(cir)
                else:
                    self.label2.setColor(QColor(255, 0, 0, 100))
                    self.label2.setText(f'陌生人')
                    self.circ.setPixmap(cir)
                    
        else:
            self.label2.setVisible(False)
            
            self.label2.clear()
            self.circ.clear()

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
            self.t  = threading.Thread(target=self.loopReco)
            self.stop = False
            self.t.start()
            #thread = threading.Thread(target=self.Reco)
            #thread.start()
    def initMysql(self):
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="123456",
          database="face"
        )

        # 创建游标对象
        self.mydb = mydb
    def loopReco(self):
        font = QFont()
        font.setBold(True)
        font.setPointSize(self.label.height()//15)
        self.label2.setFont(font)

            
        while(1):
            if self.stop:
                break
            time.sleep(0.020)
            self.Reco() 
                       
            
    '''关闭摄像头'''
    def close_camera(self):
        self.stop = True
        self.camera_timer.stop()  # 停止读取
        self.cap.release()  # 释放摄像头
        self.label.clear()  # 清除label组件上的图片
        self.label.clear()  # 清除label组件上的图片
        self.label2.setVisible(False)
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
            
            if current_widget !=self.screen:
                current_widget.store_image()
            n = len(self.Image)
            for file_name in file_names:
                pixmap = QPixmap(file_name)
                current_widget.Image.append(pixmap)
            if current_widget ==self.screen:
                self.Image = current_widget.Image  
            else: 
                current_widget.store_new_image(n)
                current_widget.show_save_image()
        

    def resizeEvent(self, event):
        # 在这里调用您想要执行的函数
        if not self.cap.isOpened() and self.isclicklook:
            self.show_save_image()
        font = QFont()
        font.setBold(True)
        font.setPointSize(self.label.height()//15)
        self.label2.setFont(font)
        super().resizeEvent(event)
    def cirCrop(self,pixmapa:QPixmap ,width):
        w = pixmapa.width()
        h = pixmapa.height()
        cropW = min(w,h)
        x = (w-cropW)//2
        y = (h-cropW)//2
        pixmapa = pixmapa.copy(x,y,x+cropW,y+cropW)
        pixmap = QPixmap(width,width)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        #painter.begin(self)         #要将绘制过程用begin(self)和end()包起来
        path = QPainterPath()
        path.addEllipse(0, 0, width, width);    #绘制椭圆
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, width, width, pixmapa)
        #painter.end()
        return pixmap
    def inticompleter(self):
        
        # 查询所有不同的 department
        query = QSqlQuery()
        query.prepare("SELECT DISTINCT department FROM user_table")
        if not query.exec():
            # 查询失败，打印错误信息
            print("Query failed:", query.lastError().text())
            return
        # 将结果添加到 department_box 中
        departments = []
        while query.next():
            department = query.value(0)
            departments.append(department)

        # 如果 department_box 中有选中的值，则查询对应的 classname


        query.prepare(f"SELECT DISTINCT classname FROM user_table ")
        if not query.exec():
            # 查询失败，打印错误信息
            print("Query failed:", query.lastError().text())
            return
        # 将结果添加到 class_box 中
        classnames = []
        while query.next():
            classname = query.value(0)
            classnames.append(classname)
        self.departmentsCompleter  = QCompleter(departments)
        self.classnamesCompleter = QCompleter(classnames)
        self.departmentsCompleter.setFilterMode(Qt.MatchContains)  
        self.departmentsCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.departmentsCompleter.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.department.setCompleter(self.departmentsCompleter)
        
        self.classnamesCompleter.setFilterMode(Qt.MatchContains)  
        self.classnamesCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.classnamesCompleter.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.classname.setCompleter(self.classnamesCompleter)
    def departmentChange(self):
        query = QSqlQuery()
        departments  = self.department.text()
        query.prepare("SELECT DISTINCT `classname` FROM user_table where department = ?")  
        query.bindValue(0, departments)
        if not query.exec():
            # 查询失败，打印错误信息
            print("Query failed:", query.lastError().text())
            return
        # 将结果添加到 class_box 中
        classnames = []
        while query.next():
            classname = query.value(0)
            classnames.append(classname)
        self.classnamesCompleter = QCompleter(classnames)
        self.classnamesCompleter.setFilterMode(Qt.MatchContains)  
        self.classnamesCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.classnamesCompleter.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.classname.setCompleter(self.classnamesCompleter)
        
class CropQLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 0
        self.color = QColor(0, 0, 0, 0) # 默认黑色背景
        
    def setColor(self, color):
        self.color = color
        self.update()
        
    def setRadius(self, radius):
        self.radius = radius
        self.update()
        
    def paintEvent(self, event):
         
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.transparent) # 填充透明色
        path = QPainterPath()
        path.moveTo(self.radius, self.height()//2)   #移动到圆弧起点
        path.arcTo(0, self.height()//2-self.radius, self.radius*2, self.radius*2, 90, 180)  #绘制半圆弧
        path.moveTo(self.width()-self.radius, self.width()//2)   #移动到圆弧起点
        path.arcTo(self.width()-self.radius*2, self.height()//2-self.radius, self.radius*2, self.radius*2, 270, 180)  #绘制半圆弧

        path.lineTo(self.radius,self.height()//2-self.radius)
        path.lineTo(self.radius,self.height()//2+self.radius)
        path.lineTo(self.width()-self.radius,self.height()//2+self.radius)

        
        path.closeSubpath()  #关闭路径
        painter.fillPath(path, self.color) # 填充路径
        painter.end()
        super().paintEvent(event)

        

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    home = Home()
    home.show()
    app.exec_()

