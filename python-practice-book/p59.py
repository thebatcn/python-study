import os
import sys

def extcount(files):
    extcount = {}
    for file in files:
        ext = file.split('.')[-1]
        extcount[ext] = extcount.get(ext, 0) + 1
    return extcount


if __name__ == '__main__':
    path = sys.argv[1]
    files = os.listdir(path)
    count_ext  = extcount(files)
    
# files = ['file1.txt', 'file2.doc', 'file3.txt', 'file4.doc', 'file5.txt']
for key,value in count_ext.items():
    print(f"{value} : {key}")