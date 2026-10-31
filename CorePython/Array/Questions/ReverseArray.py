from array import *

arr = array('i',[10,20,30,40,50,60,70])
reversed=array('i',[])
i=len(arr)-1
while i>=0:
    reversed.append(arr[i])
    i-=1
print(reversed)