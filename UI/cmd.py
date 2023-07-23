import os
import subprocess

# 指定包含 .ui 文件的文件夹和要生成的 Python 代码文件夹
ui_folder = 'UI'
py_folder = 'UI'

# 遍历 .ui 文件并使用 subprocess 运行 pyuic5 命令
for filename in os.listdir(ui_folder):
    if filename.endswith('.ui'):
        # 构建文件名和命令
        ui_path = os.path.join(ui_folder, filename)
        py_name = f"Ui_{os.path.splitext(filename)[0]}.py"
        py_path = os.path.join(py_folder, py_name)
        command = f"pyuic5 {ui_path} -o {py_path }"
        subprocess.run(command, check=True)

        print(f"{ui_path} -> {py_path}")