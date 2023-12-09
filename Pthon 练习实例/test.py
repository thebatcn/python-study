words ='d DDD sd1'
newwords=''

newwords = filter(lambda x: x.isalpha() or x==' ', words)
print(list(newwords))
# for i in words:
#     if not i.isalpha():
#         continue
#     else:
#        newwords= ''.join(i.lower())  
# print(newwords)
# W =[str.lower(w) for w in words.split() ]


# print(W)  
print(list(filter(lambda x: x.isalpha() or x==' ', words)))
#print hello world
print('hello world')
冒泡排序法


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):    
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

        