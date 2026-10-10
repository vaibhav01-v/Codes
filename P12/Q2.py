# write a program to compute the Hamming distance btn two code words

a="101101"
b="111001"
distance=0
i=0
while i < len(a):
    if a[i] != b[i]:
        distance=distance+1
    i=i+1
print("hamming distance :",distance)