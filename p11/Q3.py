# write program to compute the syndrome of recived vector
p=7
recived=[1,4,3,2,0]
# points()
points=[1,2,3,4,5]
syndrome=[]
j=1
while j<=2:
    s=0
    i=0
    while i < len(recived):
        s=(s+recived[i]*(points[i]**j))%p
        i=i+1
    syndrome.append(s)
    j=j+1
print("syndrome value :",syndrome)