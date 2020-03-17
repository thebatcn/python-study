"""命令行地址簿
通过选项，可以实现查询、新增、修改、删除功能。
"""

import os
import json


myfilename = "地址簿.txt"
myfile =None


def Main_screen():
    print("                             **************************")
    print("                             *                        *")
    print("                             *      命令行地址簿      *")
    print("                             *                        *")
    print("                             **************************")
    print("                                                         输入相应命令选项进行操作")
    print("1:查询")
    print("2:新增")
    print("3:修改")
    print("4:删除")
    print("5:退出")

"""
def readfile(r_mode):



   myfile =open(myfilename,r_mode)
   if r_mode == "r":
       for line in myfile:
           jsobj =json.loads(line)
           addata.update(jsobj)
"""

def chaxun():
    addata = {}  # 定义空字典 保存地址簿数据

    myfile = open(myfilename, "r")
    for line in myfile:
        jsobj = json.loads(line)
        addata.update(jsobj)

    while True:
        name = input("输入查询的名字：")

        if name in addata:
            for i in range(2):
                print(addata[name][i],end=" ")
        else:
            print("查询名字不存在")
            break


def xinzeng():
    addata = {}  # 定义空字典 保存地址簿数据

    myfile = open(myfilename, "a")
    name = input("输入新增人员名字：")
    age = input("输入新增人员年龄：")
    addrest = input("输入新增人员地址：")

    addata.update({name:[age,addrest]})
    jsobj =json.dumps(addata)
    myfile.write(jsobj+"\n")
  #  myfile.write(jsobj)



def xiugai():
    print("修改")

def shanchu():
    print("删除")

def tuichu():
    exit()




def run():
    if not os.path.exists(myfilename):
        print("地址簿数据库不存在,已初始化数据库")
        myfile =open(myfilename,"w")
    else:
        myfile=open(myfilename,"r")

    Main_screen()
    while True:
        inputKey = input("输入命令选项:")
        if inputKey == "1":
            chaxun()
        elif inputKey=="2":
            xinzeng()
        elif inputKey == "3":
            xiugai()
        elif inputKey == "4":
            shanchu()
        elif inputKey =="5":
            tuichu()
        else:
            print("输入不对，重新输入选项。")


run()

