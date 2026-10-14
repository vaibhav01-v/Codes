s={10,20,30,40,50,60}


print(s,type(s))

a={}
# It does not allow duplicate values
s.add(50)
s.add(25)
print(s.copy())
# s.append(a)
# s.clear()

print(s)


a={5.05,23,60,70,9,4,56}
s.update([50,10,77.88,88.77])

s.remove(77.88)
s.discard(50)


x=s.pop()

print(s.union(a))
print(s.intersection(a))
print(s.difference(a))
print(s.symmetric_difference(a))
# print(x)
