def binary_search(lst,item):
    low = 0
    high = len(lst)-1
    

    while low <= high:
        mid = int((low+high)/2)
        if lst[mid] == item:
            return mid
        
        if item > lst[mid]:
            low = mid +1
        else: 
            item < lst[mid]
            high = mid -1
    return None

my_list = [1,2,5,7,8,11,12,18]       

print(binary_search(my_list,20))

