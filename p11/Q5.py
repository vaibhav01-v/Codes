# write program to construct an altrnant code using parity check matrix derived from Grs code
p=7
points=[1,2,3,4,5]
rows=2
h=[]
r=0
while r<rows:
    row=[]
    i=0
    while i<len(points):
        value=(points[i]**r)%p
        row.append(value)
        i=i+1
    h.append(row)
    r=r+1
print("alternant parity check :")
for row in h:
    print(row)