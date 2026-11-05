from array import *

arr = array('i',[1,2,3,4,5,6,7])
reverse=[]
i=len(arr)-1
while i>=0:
    reverse.append(arr[i])
    i-=1
print(reverse)
