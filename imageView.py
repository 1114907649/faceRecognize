import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlQuery
from random import uniform
from PyQt5.QtGui import QPixmap
from UI.Ui_imageView import Ui_Form
from PyQt5.QtCore import Qt
class ImageView(QWidget,Ui_Form):
    def __init__(self,home) :
        super(ImageView,self).__init__()
        self.setupUi(self)
        self.home =home
        self.home.home.stacked_widget.addWidget(self)
        self.department.setText(self.home.value[0])
        self.classname.setText(self.home.value[1])
        self.name.setText(self.home.value[2])
        self.ID.setText(self.home.value[3])
        
        dir_path = f'./images/{self.home.value[0]}/{self.home.value[1]}/{self.home.value[3]}_{self.home.value[2]}/'    
        self.dir_pth = dir_path
        self.files_path = []
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            self.update_image_path(self.home.value[3],dir_path)
        files = os.listdir(dir_path)
        if len(files) ==0:
            self.update_image_path(self.home.value[3],dir_path)
        query = QSqlQuery()
        query.exec(f"SELECT image_path FROM user_table WHERE id = '{self.home.value[3]}'")
        self.Image = []
        self.index = 0
        self.path  = ''
        
        
        while query.next():
            self.path = query.value(0)
        file_list = self.path.split(',')
        
        file_names = file_list[1:]

        for file_name in file_names:
            file_path = f"{dir_path}/{file_name.strip()}"
            self.files_path.append(file_path)
            self.Image.append(QPixmap(file_path)) 

        self.n = len(self.Image)
        self.init()  
    def init(self):
        if len(self.Image)>0:
            self.show_save_image()
        self.back_bt.clicked.connect(self.back_fc)
        self.prev_bt.clicked.connect(self.prev_image)
        self.next_bt.clicked.connect(self.next_image)
        self.delete_bt.clicked.connect(self.delete_image)
    def back_fc(self):
        self.store_image()
        self.home.home.stacked_widget.setCurrentWidget(self.home)
    def prev_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index -1+len(self.Image))%(len(self.Image))
            self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
            self.show_save_image()
    def next_image(self):
        if(len(self.Image)>0):
            self.index  = (self.index +1)%(len(self.Image))
            self.show_save_image()
    def delete_image(self):
        if(len(self.Image)>1):
            del self.Image[self.index]
            os.remove(self.files_path[self.index])
            del self.files_path[self.index]
            self.index  = (self.index -1)%(len(self.Image))
            
            self.show_save_image()
        elif(len(self.Image)>0) :
            del self.Image[self.index]
            os.remove(self.files_path[self.index])
            del self.files_path[self.index]
            self.label.clear()
            self.current_index.clear()
    def show_save_image(self):
        self.current_index.setText('%d/%d'%(self.index+1,len(self.Image)))
        scaled_pixmap = self.Image[self.index].scaled(self.label.width()-7,self.label.height()-7, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)   
    def departmentbox_change(self):
        query = QSqlQuery()
        self.class_box.clear()
        department = self.department_box.currentText()
        if department:
            query.prepare(f"SELECT DISTINCT classname FROM user_table WHERE department = :department")
            query.bindValue(":department", department)
            if not query.exec():
                # 查询失败，打印错误信息
                print("Query failed:", query.lastError().text())
                return
            # 将结果添加到 class_box 中
            classnames = ['ALL']
            while query.next():
                classname = query.value(0)
                classnames.append(classname)
            self.class_box.addItems(classnames)  
            
            
            
            
    def conbox_init(self):
        self.department_box.clear()
        self.class_box.clear()
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
        self.department_box.addItems(departments)
        # 如果 department_box 中有选中的值，则查询对应的 classname
        department = self.department_box.currentText()

        if department:
            query.prepare(f"SELECT DISTINCT classname FROM user_table WHERE department = :department")
            query.bindValue(":department", department)
            if not query.exec():
                # 查询失败，打印错误信息
                print("Query failed:", query.lastError().text())
                return
            # 将结果添加到 class_box 中
            classnames = []
            while query.next():
                classname = query.value(0)
                classnames.append(classname)
            self.class_box.addItems(classnames)
    def resizeEvent(self, event):
        # 在这里调用您想要执行的函数
        if len(self.Image)>0:
            self.show_save_image()
        super().resizeEvent(event)
    def store_image(self):
        if self.n != len(self.Image):
            ID = self.home.value[3]
            images_path = self.dir_pth
            if  ID and images_path:
                #if not os.path.exists(images_path):
                #    os.makedirs(images_path)
                #    for i in range(len(self.Image)):
                #        self.Image[i].save(images_path+'%d.png'%(i+1))
                self.rename_images(images_path)
                for i in range(len(self.Image)):
                    images_path  =images_path+','+'%d.png'%(i+1)
                    self.update_image_path(ID,images_path)
    def update_image_path(self, ID, new_image_path):
        query = QSqlQuery()
        query.prepare("UPDATE user_table SET image_path = :image_path WHERE id = :id")
        query.bindValue(":id", ID)
        query.bindValue(":image_path", new_image_path)
        if query.exec_():
            print("Image path updated successfully")
        else:
            print("Error updating image path:", query.lastError().text())
    def rename_images(self,images_path):
        image_names = [name for name in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, name))]
        image_names.sort(key=lambda name: int(name.split('.')[0]))
        for i, old_image_name in enumerate(image_names, 1):
            old_image_path = os.path.join(images_path, old_image_name)
            new_image_name = f"{i}.png"
            new_image_path = os.path.join(images_path, new_image_name)
            os.rename(old_image_path, new_image_path)
        print("Images renamed successfully")
    def store_new_image(self,n):    
        save_path = self.dir_pth
        if save_path:
            department = self.home.value[0]
            classname = self.home.value[1]
            username = self.home.value[2]
            ID = self.home.value[3]
            images_path = save_path
            for i in range(n):
                images_path  =images_path+','+'%d.png'%(i+1)
                self.Image[i].save(save_path+'%d.png'%(i+1))
            for i in range(n,len(self.Image)):
                images_path  =images_path+','+'%d.png'%(i+1)
                self.Image[i].save(save_path+'%d.png'%(i+1))
            query = QSqlQuery()
            self.update_image_path(ID,images_path)
            
            #query.exec_("INSERT INTO user_table VALUES ('%s', '%s', '%s', '%s','%s')"%(department,classname,username,ID,images_path))