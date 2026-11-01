from array import *

arr = array('i', [45, 12, 89, 23, 5, 67, 100, 3])
largestNo=arr[0]
smallNo=arr[0]
for i in arr:
    if i > largestNo:
        largestNo = i

    if i < smallNo:
        smallNo = i

print(largestNo)
print(smallNo)
