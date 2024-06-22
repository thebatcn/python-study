import sys
# 获取命令行参数
file = sys.argv[1]

def parse_csv(file):
    # 打开文件
    fp = open(file)
    # 初始化结果列表
    result =[]
    
    # 遍历文件每一行
    for line in fp:
        # 将每一行添加到结果列表中，并去除行尾的换行符
        result.append(list(line.strip().split()))
    # 返回结果列表
    return result
    
# 调用函数
print(parse_csv(file))