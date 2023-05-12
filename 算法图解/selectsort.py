def findsmallest(arr):
 smallest_value = arr[0]
 smallest_index = 0
 
 for i in range(1,len(arr)):
  if arr[i] < smallest_value:
   smallest_value = arr[i]
   smallest_index = i
   print("i: ", i)
 return smallest_index
   
 #return (smallest_index, smallest_value)
   
myarr = [1,3,7,16,2,-22,5,0,-15]

print(findsmallest(myarr)) 

def selectsort(arr):
 newarr = []
 
 k = len(arr)
 for j in range(k):
  small_id = findsmallest(arr)
  newarr.append(arr.pop(small_id))
  print('j: ',j)
 return newarr
  
        
print(selectsort(myarr))       
   