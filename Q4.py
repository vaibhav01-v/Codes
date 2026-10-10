# write py program to generate all elements of the factoring for given integer q , n and display each elements in polynomial form

# q=int(input("q"))
# n=int(input("n"))
import math 
q=int(input("enter q :"))
n=int(input("enter n :"))
vects=[]
for i in range (q**n):
    vec=[]
    temp=i
    
    
    for j in range (n):
        vec.insert(0,temp%q)
        temp=temp//q
    # vector_str=" ".join(str(digit)for digit in vec )
    vects.append("".join(map(str,vec)))
    
print(vects) 


for v in vects:
    poly=[]
    for i,c in enumerate(v):
        c=int(c)
        # print(i,c)
        if c != 0:
            if i==0:
                term="1"
            elif i==1:
                term="x" 
            else :  
                term="x^"+str(i) 
            if c>1 :
                   term = "x^" + str(i)
                # term=(c)+term             
            poly.append(term) 
    print(v, "->", " + "," ".join(poly) if poly else "0")
g=list(eval(input(f"Enter {n} coefficient saperated by commas  :")))
ideal=[]
for r in vects:
    product=[]
    if product in ideal:
        for k in range(n):
            product.append((r[i]*g[i])%q)
        if product not in ideal:
            ideal.append(product)    
for v in ideal:
    polys=[]
    for i,c in enumerate(v):
        c=int(c)
        # print(i,c)
        if c != 0:
            if i==0:
                term="1"
            elif i==1:
                term="x" 
            else :  
                term="x^"+str(i) 
            if c>1 :
                   term = "x^" + str(i)
                # term=(c)+term             
            polys.append(term) 
    print(v, "->", " + "," ".join(polys) if polys else "0")