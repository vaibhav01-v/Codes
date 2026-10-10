# write a py program to compute parity check polynomial

# Compute Parity Check Polynomial

n = int(input("Enter n: "))
g = list(eval(input("Enter generator polynomial (like [1,0,1,1]): ")))

# Create x^n - 1  →  [1,0,0,...,0,1]
xn1 = [1] + [0]*(n-1) + [1]

temp = xn1[:]
quotient = []

while len(temp) >= len(g):
    if temp[0] == 1:
        quotient.append(1)
        for i in range(len(g)):
            temp[i] = temp[i] ^ g[i]   # XOR operation
    else:
        quotient.append(0)
    temp.pop(0)

print("\nParity Check Polynomial Coefficients:")
print(quotient)