from array import *

# how to merge two array 


arr=array('i',[10,20,30,40,50,60])
arr1=array('i',[70,80,90])

# print(arr,arr1 )

merge=[]
split=[]
for i in arr:
    merge.append(i)
for j in arr1:
    merge.append(j)


a=0
print(merge)
for i in merge:
    print(i)