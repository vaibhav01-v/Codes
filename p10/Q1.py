# write py program to compute the set of quadratic residues and non residue modulo a prime p
p=13
q=[]
n=[]
a=1
while a<p:
    r=(a*a) % p
    if r not in q:
        q.append(r)
    a=a+1
x=1
while x<p:
    if x not in q:
        n.append(x)
    x=x+1
print("quadratic residue : ",q) 
print("quadratic non-residue : ",n) 
 