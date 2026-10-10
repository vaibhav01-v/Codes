# write a python program to compute reciprocal of polynomial and display it in polynomial form.

deg = int(input("enter degreee  :"))
g=list(eval(input("enter geberator :")))

print("Original polynomial")
poly= " "
for i in range(len(g)):
    if g[i]==1:
        if i==0:
            poly +=" 1 "
        elif i==1:
            poly +="+x"
        else :
            poly +="+x^"+str(i)
print(poly)
reci=[]
for i in range(len(g)-1,-1,-1):
    reci.append(g[i])
    
recpoly=" "
for i in range(len(reci)):
    if reci[i] == 1:
        if i == 0:
            recpoly += "1"
        elif i == 1:
            recpoly += " + x"
        else:
            recpoly += " + x^" + str(i)
print(recpoly)