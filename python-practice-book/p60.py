import os

path = r'C:\Users\Administrator\Documents\小升初数学'

files = os.listdir(path)
stat  ={}

for file in files:
    stat_result = os.stat(os.path.join(path, file))
    stat[file] = stat_result.st_size, stat_result.st_mtime,stat_result.st_ctime

print(stat)

# 输出结果：