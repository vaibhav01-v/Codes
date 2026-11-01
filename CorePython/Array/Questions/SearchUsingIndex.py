from array import *
arr= array('i',[])
n=int(input("Enter the no :"))
for i in range(n):
    x=int(input("Enter the No :"))
    arr.append(x)
print(arr)
    # print(i)

search=int(input("search the Element :"))
increment=0
for e in arr:
    if e==search:
        print(increment)
        break
    increment+=1