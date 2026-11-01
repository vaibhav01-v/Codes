from array import *

arr = array('i', [10, 20, 10, 30, 20, 10, 40])
seen=[]
for i in range(len(arr)):
    if(arr[i] not in seen):
        times=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                
                times+=1
        print(arr[i],times)
        seen.append(arr[i])
# arr.count()
# print(arr)
# for i in arr:
#     if 