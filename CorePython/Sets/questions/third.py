s=set()
s.add(20)
s.add(30)
s.add(60)
s.add(45)
s.update([32])
print(type(s),s)
s.discard(45)
print(s,len(s))


print(s)
print(20 in s)

