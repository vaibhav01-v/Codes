lst = [10, 20, 30, 10, 40, 20, 50, 30]
dup=set()
for i in lst:
    if i>1:
        dup.add(i)
print(dup)