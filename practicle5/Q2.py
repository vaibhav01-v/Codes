# write py program to construct the generator matrix by cyclic shifting generator polynomial of binary cyclic code.

import math
n =int(input("enter n "))
deg=int(input("enter degree"))
g=list(eval(input("Enter generator  ")))
k=n-deg

row = g+[0]*(n-len(g))
for i in range(k):
    print(row)
    last=row[-1]
    row=[last]+row[:-1]