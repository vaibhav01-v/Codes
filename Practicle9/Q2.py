# write a program to detect wheather error occured in recived word using Rs code

mod=7
print("enter 3 message symbol(0-6):")
r=[]
for i in range(6):
    r.append(int(input()))

s1=0
s2=0
s3=0

for i in range(6):
    s1=(s1+r[i]*(1**i))% mod
    s2=(s2+r[i]*(2**i))% mod
    s3=(s3+r[i]*(3**i))% mod
print("syndrome :")
print("s1 =",s1)
print("s2 =",s2)
print("s3 =",s3)
 
if s1 == 0 and s2 == 0 and s3 == 0:
    print("No error ")
else:
    print("Error detected ")