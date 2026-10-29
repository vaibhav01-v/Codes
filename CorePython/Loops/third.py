i=0
n=6
while(i<n):
    j=0
    while(j<n):
        if(j<i):
            print(j,end=" ")
        else:
            print(i,end=" ")
        j+=1
    print()
    i+=1