import os
import sys

def list_files(path):
    # 列出指定目录的所有文件列表
    files = os.listdir(path)
    return files

# path = sys.argv[1]
# print(path)

#列出指定目录的所有文件列表

# 获取当前工作目录
# current_dir = os.getcwd()
# print("当前工作目录:", current_dir)

# print(list(os.scandir(current_dir)))
# os.scandir(current_dir)

# # 切换到指定目录
# os.chdir('C:/Users/Administrator/Desktop')
# print("切换后的目录:", os.getcwd())

# # 创建新目录
# os.mkdir('test')
# print("新目录已创建")        

# # 删除目录
# os.rmdir('test')
# print("目录已删除")

# 列出当前目录下的所有文件和文件夹
# files = os.listdir(path)
# for file in files:
#     print(file)

# # 重命名文件    
