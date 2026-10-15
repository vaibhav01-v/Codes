
# Check whether one set is a subset of another.

set1={10,20,30,40,50}
set2={10,20,30,40,50,60}
print(set1 in set2)
print(set1.issubset(set2))

a={1,2,3,4}
b={1,2,3,4,5}

# the logis 
print(a.issubset(b))

# Question: Are all elements of a present in b?

# 1 → Present in b ✅
# 2 → Present in b ✅
# 3 → Present in b ✅


# Question: Are all elements of b present in a?

# 1 → Present in a ✅
# 2 → Present in a ✅
# 3 → Present in a ✅
# 4 → Not present in a ❌
# 5 → Not present in a ❌
print(b.issubset(a))
