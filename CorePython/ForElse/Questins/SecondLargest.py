s = {10, 50, 30, 90, 70, 80}
largest=0
second_largest=0
for i in s:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i
print(largest)
print(second_largest)
