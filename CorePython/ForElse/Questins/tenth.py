s = {"python", "java", "hello"}
# for i in s:
#     rev="".join(reversed(i))
#     print(rev)
        


for i in s:
    rev=""
    for j in i:
        rev = j + rev
    print(rev)
