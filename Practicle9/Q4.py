# write progam to simulate erasure (known errror position )using Rs code

mod=7
print("enter 3 message symbol(0-6):")
r=[]
for i in range(6):
    r.append(int(input()))
print("Erassure position :")
for i in range(6):
    if r[i]==-1:
        print("Erassure position :",i)
print("rs code can correct up to 3 erassure ")        
