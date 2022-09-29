import numpy as np

arr = np.arange(10)
np.save('some_array',arr)

arr_1 = np.arange(10,21)
arr_2 = np.array(list('ABCD'))
print(np.load('some_array.npy'))

np.savez('array_archive',arr_2,a=arr,b=arr_1) #位置参数和关键字参数

arch = np.load('array_archive.npz')
print(arch['b'])
print(arch['a'])
print(arch['arr_0']) #位置参数 arr_0,arr_1以此类推
# help(np.savez)
