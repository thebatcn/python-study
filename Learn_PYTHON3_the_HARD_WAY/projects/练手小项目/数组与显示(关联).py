ab=[]

for i in range(5):
    for j in range(5):
        if i==j or i == (4-j):
            print('1',end="")
            ab.append((i,j))
        else:
            print('0',end=' ')
    print()

print(ab)

for i in range(5):
    for j in range(5):
        print('.',end=' ')
    print()


N = 6  # 总行数
M = 6  # 总列数

# 外层循环控制行
for i in range(N):
    # 内层循环控制列
    for j in range(M):
        # 首先判断是否是边框位置或者中心位置
        if i == 0 or i == N - 1 or j == 0 or j == M - 1 or (i == N // 2 and j == M // 2):
            print("1", end="")
        # 如果不是边框位置或者中心位置，则判断是否在正方形的四条边上
        elif (i == 1 and 1 <= j <= M - 2) or (i == N - 2 and 1 <= j <= M - 2) or \
                (j == 1 and 1 <= i <= N - 2) or (j == M - 2 and 1 <= i <= N - 2):
            print("1", end="")
        # 如果不在正方形的四条边上，则是正方形的内部，输出"*"
        else:
            print("*", end="")
    print()  # 换行