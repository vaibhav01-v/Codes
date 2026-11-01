from array import *
arr = array('i', [10, -5, 0, 20, -15, 0, 30, -2])
positiveNo=0
negativeNo=0
zero=0
for i in arr:
    if i>0:
        # positiveNo.append(i)
        positiveNo+=1
    elif(i<0):
        # negativeNo.append(i)
        negativeNo+=1
    elif i==0:
        zero+=1
print(positiveNo)
print(negativeNo)
print(zero)