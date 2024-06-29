def array(rows, columns):
    '''创建一个二维数组'''
    return [[None for _ in range(columns)] for _ in range(rows)]

# 测试  
# array_2d = array(3, 4)
# for row in array_2d:    
#     print(row)
    
# 输出: 
# [0, 0, 0, 0]

print(array(3, 4))