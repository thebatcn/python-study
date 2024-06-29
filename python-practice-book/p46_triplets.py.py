# 定义一个函数triplets，用于计算小于n的三个数的组合
def triplets(n):
    # 返回一个列表，列表的元素为元组，元组的元素为三个数，满足i+j<n的条件
    result = [(i,j,i+j) for i in range(1,n) for j in range(i,n) if i+j < n ]
    # 返回结果
    return result
   

# 输入n的值
n = int(input("Enter the value of n: "))
# 调用函数triplets，计算小于n的三个数的组合
triplets = triplets(n)
# 打印结果
print("Triplets less than", n, "are:", triplets)