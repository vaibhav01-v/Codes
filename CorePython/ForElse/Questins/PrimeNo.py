num=int(input("Enter the no :"))
# for i in range (2,num):
#     if num%i==0:
#         print(i,"it is prime")

count=0
for i in range(1,num+1):
    if(num%i==0):
        count +=1
        count==2
        print( i,"Prime NO :")
else:
    print(i,"not PRime")




num = int(input("Enter number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")