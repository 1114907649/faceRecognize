import pickle
from PyQt5 import  QtWidgets
from PyQt5.QtSql import QSqlQuery
import numpy as np
from UI.Ui_database import Ui_database
from DB.UserDB import userDB
from imageView import ImageView
from feature.deleFt import deleF
import os
class Database(QtWidgets.QWidget,Ui_database):
    def __init__(self,home) :
        super(Database,self).__init__()
        self.setupUi(self)
        self.home = home
        self.db=userDB()
        self.tableView.setModel(self.db.model)
        self.home.stacked_widget.addWidget(self)
        self.value =  ''
        self.conbox_init()
        self.init()

        
    


    def init(self):

        
        self.tableView.clicked.connect(self.show_value)
        self.back_bt.clicked.connect(self.back)
        self.refresh_bt.clicked.connect(self.refresh)
        self.view_bt.clicked.connect(self.look_image)
        self.delete_bt.clicked.connect(self.delete_fc)
        self.add_bt.clicked.connect(self.add_row)
        self.tableView.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.department_box.currentTextChanged.connect(self.departmentbox_change)
        self.class_box.currentTextChanged.connect(self.classbox_change)
        self.look_bt.clicked.connect(self.look_fc)
        
    def look_fc(self):
        department = self.department_box.currentText()
        classname = self.class_box.currentText()
        name = self.name_input.text().strip()
        ID = self.ID_input.text().strip()
    
        # 构造过滤器字符串
        filter_str = ""
        #filter_str开头不AND
        T = ''
        if department != 'ALL':
            filter_str += f"department = '{department}'"
            T = 'AND'
        if classname != 'ALL':
            filter_str += f" {T} classname = '{classname}'"
            T = 'AND'
        if name != "":
            filter_str += f" {T} username LIKE '%{name}%'"
            T = 'AND'
        if ID != "":
            filter_str += f" {T} ID LIKE '%{ID}%'"
    
        # 如果过滤器字符串为空，则显示全部记录
        if filter_str == "":
            self.db.model.setFilter("")
        else:
            self.db.model.setFilter(filter_str)
    
        # 重新查询并更新模型
        self.db.model.select()
        
    def departmentbox_change(self):
        query = QSqlQuery()
        self.class_box.clear()
        department = self.department_box.currentText()
        if department=='ALL':
            query.prepare(f"SELECT DISTINCT classname FROM user_table ")
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
        elif department:
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
        self.name_input.clear()
        self.ID_input.clear()
    def classbox_change(self):
        if self.department_box.currentText()=='ALL':
            query = QSqlQuery()
            classname = self.class_box.currentText()
            department = ''
            if classname!='ALL':
                query.prepare(f"SELECT DISTINCT department FROM user_table WHERE classname = :classname")
                query.bindValue(":classname", classname)
                if not query.exec():
                    # 查询失败，打印错误信息
                    print("Query failed:", query.lastError().text())
                    return
                while query.next():
                    department = query.value(0)
            if department :    
                self.department_box.setCurrentText(department) 
                self.departmentbox_change()
                self.class_box.setCurrentText(classname)   
        self.name_input.clear()
        self.ID_input.clear()   
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
        departments = ['ALL']
        while query.next():
            department = query.value(0)
            departments.append(department)
        self.department_box.addItems(departments)
        # 如果 department_box 中有选中的值，则查询对应的 classname
        department = self.department_box.currentText()
        if department=='ALL':
            query.prepare(f"SELECT DISTINCT classname FROM user_table ")
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
        elif department:
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
    def look_image(self):
        if self.value:
            self.imageView = ImageView(self)
            self.home.stacked_widget.setCurrentWidget(self.imageView)
            if len(self.imageView.Image)>0:
                self.imageView.show_save_image()
    def on_selectionChanged(self, selected, deselected):
        # 获取最后一个选中单元格的行标
        indexes = selected.indexes()
        if indexes:
            last_index = indexes[-1]
            row = last_index.row()
            self.show_fc(row)

    def show_value(self):
        index= self.tableView.currentIndex()
        row = index.row()
        self.show_fc(row)

    def show_fc(self,row):
        model = self.tableView.model()
        department = model.data(model.index(row, 0))
        classname = model.data(model.index(row, 1))
        name = model.data(model.index(row, 2))
        id = model.data(model.index(row, 3))
        
        self.value = [department, classname, name,id ]
        self.department_box.setCurrentText(department)
        self.class_box.setCurrentText(classname)
        self.name_input.setText(name)
        self.ID_input.setText(id)
    def refresh(self):
        #self.db.model.submitAll()
        #self.db=userDB()
        #self.tableView.setModel(self.db.model)
        self.db.model.select()
    def back(self):
        with open('feature/feature.pickle', 'rb') as f:
            pids ,img_feats = pickle.load(f)
        self.home.recogniser.labels_vis=pids
        self.home.recogniser.feat_vis = img_feats
        self.home.stacked_widget.setCurrentWidget(self.home.screen)
    def delete_fc(self):
        selected_rows = self.tableView.selectionModel().selectedRows()
        if selected_rows :
            for row in sorted(selected_rows, reverse=True):
                model = self.tableView.model()
                num = model.data(model.index(row.row(), 3))
                deleF(num)
                self.delete_images(num)
                self.tableView.model().removeRow(row.row())
        # 更新 QTableView 中的视图
        else :
            row= self.tableView.currentIndex()
            model = self.tableView.model()
            num = model.data(model.index(row.row(), 3))
            self.delete_images(num)
            deleF(num)
            self.tableView.model().removeRow(row.row())
        self.db.model.select()
        self.value = ''
        self.name_input.setText('')
        self.ID_input.setText('')
    def add_row(self):
        print(self.tableView.model().rowCount())
        self.tableView.model().insertRow(self.tableView.model().rowCount())
        
    def store(self):
        pass
    def delete_images(self, ID):
        query = QSqlQuery()
        query.prepare("SELECT image_path FROM user_table WHERE id = :id")
        query.bindValue(":id", ID)
        if query.exec_():
            if query.next():
                image_paths = query.value(0)
                if image_paths:
                    folder_path, *image_names = image_paths.split(',')
                    for image_name in image_names:
                        image_path = os.path.join(folder_path, image_name)
                        if os.path.exists(image_path):
                            os.remove(image_path)
                            print(f"{image_path} has been deleted.")
                        else:
                            print(f"{image_path} does not exist.")
                    print("Images deleted successfully")
                else:
                    print("No image paths found for given ID")
            else:
                print("No record found for given ID")
        else:
            print("Error retrieving image paths:", query.lastError().text())
