# write py program that determind the dimevien K of linear code C based on its generator polynomial

import math 
n = int(input("Enter code length n: "))

poly = list(eval(input("enter generator ")))
degree = len(poly) - 1

k = n - degree

print("g(x) =", degree)

print(" K =", k)



