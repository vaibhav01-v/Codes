from array import *

arr = array('i',[10,20,30,40,50,60,70])
larestNo=arr[0]
second=arr[0]
for i in arr:
    if i>larestNo:
        second=larestNo
        larestNo=i
    elif i > second:
        second=i
        
# print(larestNo)
print(second)

