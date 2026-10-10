d_values = [8, 6, 6, 6]
names = ["Hadamard", "Nordstrom-Robinson", "Preparata", "Kerdock"]

i = 0

while i < len(d_values):
    d = d_values[i]

    t = (d - 1) // 2   # error correcting capability

    print(names[i], "code corrects", t, "errors")

    i = i + 1