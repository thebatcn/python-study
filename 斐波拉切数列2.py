def fbl(n): #斐波拉切数列
    fb = []
    if n < 0:
        print('输入大于0的数字')
    if n == 0:
        fb.append(0)
    elif n ==1:
        fb.append(0)
        fb.append(1)
    else: 
        fb.append(0)
        fb.append(1)
        for x in range(2,n):
            fb.append(fb[x-2]+fb[x-1])
    return fb


print(fbl(1))