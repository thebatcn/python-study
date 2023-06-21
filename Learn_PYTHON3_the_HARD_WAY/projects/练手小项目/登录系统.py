import json
import os


# 获取当前脚本文件的绝对路径
script_path = os.path.abspath(__file__)
print("当前脚本文件的地址：", script_path)

# 获取当前脚本文件所在的目录路径
script_dir = os.path.dirname(script_path)
print("当前脚本文件所在的目录地址：", script_dir)

filename = "data.json"

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

thisfile = os.path.join(script_dir, filename)
with open(thisfile, 'w') as fp:
    json.dump(data, fp)


def load_user_data():
    with open(thisfile, 'r') as fp:
        mydata = json.load(fp)
    print(mydata)


load_user_data()

print(os.path.getsize(thisfile))

