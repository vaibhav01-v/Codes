# tupple is collection of multiple value just like a list but main diff is 
# tupple is immutable once we create we cannot change its elements

# a=(1,"vaibhav",78787,"hfjskdhf",487.888,"vaibhav")

# print(a.count("vaibhav"))
# new=(1,2,3,4,5,6,7)

# print(new.index(2))

# print(new.sort())

a=(1,2,3,4,5,6,7)
b=(1,2,3,4,5,6,7)
c=()
c=a+b
print(c)
c.index(6)
print((7 in c),c.count(7))
print(sum(c))
print(min(c))
print((c[1:3]))
print(max(c))
for i in c:
    print(i)
    print(c)
# print(type(a))
# a = new.pop(1)
# print(a)

# new.append(1)

# print(new.index(1))
print(len(c))