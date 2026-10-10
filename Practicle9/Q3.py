# write program to introduce error and check detection using Rs code

mod=7
print("enter 3 message symbol(0-6):")
c=[]
for i in range(6):
    c.append(int(input()))
pos = int(input("Enter error position (0-5)"))
val=int(input("enter error  value"))

c[pos]=(c[pos]+val)%mod

print("recived word")
print(c)

s1=0
s2=0
s3=0

for i in range(6):
    s1=(s1+c[i]*(1**i))% mod
    s2=(s2+c[i]*(2**i))% mod
    s3=(s3+c[i]*(3**i))% mod

print("syndrome :")
print("s1 =",s1)
print("s2 =",s2)
print("s3 =",s3)
    
if s1 == 0 and s2 == 0 and s3 == 0:
    print("No error ")
else:
    print("Error detected ")