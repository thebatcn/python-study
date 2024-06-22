def myenumerate(iterable, start=2):
    # 创建一个迭代器对象
    for i in iterable:
        result = i, start
        start += 1
        yield result
    
    
print(list(myenumerate("abcdef",1)))