from array import *

arr = array('i', [10, 20, 10, 30, 20, 10, 40])
seen = array('i', [])
for i in range(len(arr)):
    count=0

    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
    seen.append(i)
    print(arr[i],count)

    