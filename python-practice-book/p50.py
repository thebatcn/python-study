import re
import sys

sep = '['+(''.join(sys.argv[2:]))+']'
file = sys.argv[1]

print(sep)

def parse_csv(file,sep):
    # 打开文件
    fp = open(file)
    # 初始化结果列表
    result =[]
    
    # 遍历文件每一行
    for line in fp:
        # 将每一行添加到结果列表中，并去除行尾的换行符
        
        lst_split = re(sep,line.strip())
        result.append(lst_split)
    # 返回结果列表
    return result
    
# 调用函数
# print(parse_csv(file,sep))