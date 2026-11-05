from array import *

arr = array('i',[1,2,3,4,5,6,7])

largest=arr[0]
secondLargest=arr[0]
for i in arr:
    if i>largest:
       largest=i
    elif i > secondLargest and i != largest:
        secondLargest=largest
print(largest)
print(secondLargest)
    