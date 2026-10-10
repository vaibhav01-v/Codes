import math 
c =["000","101","010","011"]
cyclic=True
for w in c:
    y=w[-1]+w[0]+w[1]
    print(w, "  to  ",y)
    if y not in c :
        cyclic = False
if cyclic:
    print("C is cyclic")
else:
    print("C  is not cyclic")
       