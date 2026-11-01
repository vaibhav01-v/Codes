from array import *
arr = array('i', [10, 15, 20, 25, 30, 35, 40])
a=list()
sum=0
for i in arr:
    if(i%2==0):
        a.append(i)
        
print(a)
for j in a:
    sum=sum+j
print(sum)      # print(sum)
        # sum=sum=i
        # print(sum)