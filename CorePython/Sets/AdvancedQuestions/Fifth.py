numbers = [10, 20, 30, 10, 40, 20, 50, 30, 60, 20]
count=set()
count2=set()
for num in numbers:
    if num in count:
        count2.add(num)
    else:
        count.add(num)
print(count2)