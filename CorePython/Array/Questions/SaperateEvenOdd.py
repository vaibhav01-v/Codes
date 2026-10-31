from array import *
arr = array('i', [10, 15, 20, 25, 30, 35, 40])
even=set()
print(type(even))
odd=set()
print(type(odd))

for i in range(len(arr)):
    if arr[i]%2==0:
        even.add(arr[i])
    elif arr[i]%2==1:
        odd.add(arr[i])
print(even)
print(odd)