mod=7
g=[6,1,3,1]
print("enter 3 message symbol(0-6):")
m0=int(input("enter m0 :"))
m1=int(input("enter m1 :"))
m2=int(input("enter m2 :"))
message=[m0,m1,m2]
codeword = [0]*6
for i in range(3):
    for j in range(4):
        codeword[i+j]=(codeword[i+j] + message[i]*g[j])%mod
print("encoded Codeword : ")
print(codeword)
        