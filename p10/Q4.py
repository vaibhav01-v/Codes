# write program to construct the generator polynomial using quadratic residue
q=[1,2,4]
p=7
poly=['0']*p
i=0
while i < len(q):
    poly[q[i]]='1'
    i=i+1
poly[0]='1'
print("generator polynomi represntion ")
print(''.join(poly))
