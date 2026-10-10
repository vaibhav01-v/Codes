# write a py program to decode a received word using nearest neighbour decoding

received = "111100"
codebook = ["000000", "111111", "101010", "010101"]

best = ""
bestdistance = 100

i = 0
while i < len(codebook):
    c = codebook[i]
    distance = 0

    j = 0
    while j < len(c):
        if c[j] != received[j]:
            distance = distance + 1
        j = j + 1

    if distance < bestdistance:
        bestdistance = distance
        best = c   

    i = i + 1

print("Decoded codeword:", best)