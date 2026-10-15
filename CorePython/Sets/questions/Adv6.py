# Find the elements that appear in the first list but not the second.


list1=[10,20,30,40,50]
list2=[30,40,60,70,80,90]

set1=set(list1)
set2=set(list2)


print(set1.difference(set2))