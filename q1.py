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
    vector_str=" ".join(str(digit)for digit in vec )
    vects.append(vector_str)
print(vects) 























         