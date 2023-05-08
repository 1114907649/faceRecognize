# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel
from PyQt5.QtCore import Qt
import os
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
class userDB:
    def __init__(self) :
        self.db = QSqlDatabase.addDatabase("QODBC");
        self.db.setHostName("127.0.0.1")
        self.db.setPort(3306)
        self.db.setDatabaseName("face")
        self.db.setUserName("root")
        self.db.setPassword("123456")
        ok = self.db.open()


        if (ok):
                print("yes!!!")
        else :
                print("no!!!")
        #self.user_table  = QSqlTableModel()
        #query = QSqlQuery()
        #query.exec_("SELECT * FROM user_table")
        #self.user_table.setQuery(query)
        
        model = QSqlTableModel()
        model.setTable('user_table')
        model.select()
        image_path_index = model.fieldIndex('image_path')
        keyID_index = model.fieldIndex('keyID')
        model.removeColumns(image_path_index,1)
        model.setHeaderData(model.fieldIndex('department'), Qt.Horizontal, '学院')
        model.setHeaderData(model.fieldIndex('classname'), Qt.Horizontal, '班级')
        model.setHeaderData(model.fieldIndex('id'), Qt.Horizontal,'学号')
        model.setHeaderData(model.fieldIndex('username'), Qt.Horizontal,'姓名')


        self.model = model
        self.model.submitAll()
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
                        os.remove(image_path)
                    print("Images deleted successfully")
                else:
                    print("No image paths found for given ID")
            else:
                print("No record found for given ID")
        else:
            print("Error retrieving image paths:", query.lastError().text())
#a=userDB()
#print(a.tableWidget)
#app.exec_()