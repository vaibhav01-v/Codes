from array import *
arr = array('i',[1,2,3,5,6,7])
number=0
for i in range(1,8):
    if i not in arr:
        print(i)