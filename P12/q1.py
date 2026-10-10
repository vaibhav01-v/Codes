m=3
code=[]
i=0
while i < 2**m:
    word=""
    j=0
    while j< m:
        bit=(i>>j)&1
        word = word+str(bit)
        j=j+1
    code.append(word)
    i=i+1
print("hadmard code")
print(code)
