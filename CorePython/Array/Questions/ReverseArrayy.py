from array import *

arr = array('i', [45, 12, 89, 23, 5, 67, 100, 3])
# reversed=[]
# i=len(arr)-1
# while i>=0:
#     reversed.append(arr[i])
#     i-=1
# print(reversed)

reversed=[]
for i in range(len(arr)-1,-1,-1):
    if i>=0:
        reversed.append(arr[i])
print(reversed)