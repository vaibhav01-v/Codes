from array import *
arr = array('i',[10,20,30,40,50,60,70])
firstNo=0
secondNo=0

for i in arr:
    if i>firstNo:
        secondNo =firstNo
        firstNo=i
        # i.add(fistNo)
    elif i>secondNo:
        secondNo=i
print(firstNo)
print(secondNo)
sum = firstNo + secondNo

print("Sum:", sum)