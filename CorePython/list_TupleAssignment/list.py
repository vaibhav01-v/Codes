li=[]
while len(li)<4:
    no = int(input("Enter the no : "))
    li.append(no)
    print(li)
print("The total of marks is :" ,sum(li))
print(type(li))