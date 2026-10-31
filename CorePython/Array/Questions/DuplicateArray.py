from array import *

# arr = array('i',[10,20,30,40,50,60,70])
arr = array('i', [10, 20, 30, 10, 40, 20, 50])
arr1=array('i',[])
for i in range(len(arr)):
    for j in range(i):
        if arr[i] == arr[j]:
            arr1.append(arr[i])
print(arr1)