student=[]
while len(student)<3:
    name=input("Enter the name....")
    marks=int(input("Enter the Marks...."))
    student.append({"name":name,"marks":marks})
    # if marks != int :
    # # student.append()df
    #     print("Enter the No value")
    # # print(student)
    
    # for i in (student):
    student.sort()
    print(student)
