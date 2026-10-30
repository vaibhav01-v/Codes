s = {10, 15, 20, 25, 30, 35, 40}
even=0
odd=0
for i in s:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1

print(even)
print(odd)