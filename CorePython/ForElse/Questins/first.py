set=(10,20,30,"vaibhav","rahul","kunal","sumit",10.20,30.20,450,44.5)

for i in set:
    if isinstance (i,int):
        i.find(int(45))
        print(i)
    elif isinstance(i,float):
        print(i)
