# write program to encode a message polynomial using Reed solomon encoding
p=7
s0=1
s1=2
s2=1
points=[1,2,3,4,5]
codeword=[]
i=0
while i<len(points):
    x=points[i]
    value=(s0+s1*x+s2*(x*x))%p
    codeword.append(value)
    i=i+1
print("encoded Reed-solomomm codeword :")
print(codeword)