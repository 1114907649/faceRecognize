
import os
import shutil
import pymysql

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='face',
    charset='utf8mb4'
)

# 创建游标
cursor = conn.cursor()
print('yes')
# 设置图片文件夹路径
image_folder = './ttt'
i=0
# 遍历图片文件夹中的所有文件
for filename in os.listdir(image_folder):
    # 分离文件名和扩展名
    i+=1
    name, ext = os.path.splitext(filename)
    # 检查扩展名是否为 .jpg
    if ext == '.png' or ext == '.jpg':
        # 分离学院、班级、学号和图片编号
        department, classname, ID, image_number = name.split('_')
        username = f'张三{i}'
        # 设置新的图片路径
        new_image_folder = f'./images/{department}/{classname}/{ID}_{username}/'
        # 如果新的图片文件夹不存在，则创建它
        if not os.path.exists(new_image_folder):
            os.makedirs(new_image_folder)
        # 获取新的图片文件夹中现有图片的数量
        image_count = len(os.listdir(new_image_folder))
        # 设置新的图片名称
        new_image_name = f'{image_count + 1}.png'
        image_path = new_image_folder
        for j in range(image_count+1):
            image_path+=f',{j+1}.png'
        # 设置新的图片路径
        new_image_path = os.path.join(new_image_folder, new_image_name)
        # 将旧图片移动到新位置
        #os.rename(os.path.join(image_folder, filename), new_image_path)
        shutil.copy2(os.path.join(image_folder, filename), new_image_path)
        # 将图片信息插入到数据库中
        sql = f"""
            INSERT INTO user_table (department, classname, username, id, image_path)
            VALUES ('{department}', '{classname}', '{username}', '{ID}', '{image_path}')
            ON DUPLICATE KEY UPDATE
            department = VALUES(department),
            classname = VALUES(classname),
            username = VALUES(username),
            image_path = VALUES(image_path)

            """ 
        cursor.execute(sql)

# 提交更改并关闭连接
conn.commit()
conn.close()
