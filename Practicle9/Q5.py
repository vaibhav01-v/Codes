# write py program to simulate brust error of length 2 using Rs code

mod=7
print("enter 3 message symbol(0-6):")
c=[]
for i in range(6):
    c.append(int(input()))
start=int(input("Enter brust (0-4) :"))

c[start]=(c[start]+3)%mod
c[start+1]=(c[start+1]+4)%mod

print("After brust error :")
print(c)
print("Rs [6,3,4], code can correct 1 random error or 3 errasure")