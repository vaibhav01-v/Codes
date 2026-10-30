s = {10, "python", 20, "java", 30, "react"}
a=set()
for i in s:
    if isinstance(i,str):
        a.add(i)
print(a) 