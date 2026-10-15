numbers = [10, 20, 30, 20, 40, 10, 50, 30]
s=set()
d=set()
for num in numbers:
    if num in s:
        d.add(num)
    else:
        s.add(num)
print(d)