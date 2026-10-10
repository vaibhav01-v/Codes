# write program to verify that the no quadratic residue equal

p=int(input())
q=[]
# n=[]
a=1
while a<p:
    r=(a*a) % p
    if r not in q:
        q.append(r)
    a=a+1
# x=1
# while x<p:
#     if x not in q:
#         n.append(x)
#     x=x+1
print("quadratic residue : ",q) 
print("No of residue : ",len(q)) 
print("Expected =", (p-1)//2)
 