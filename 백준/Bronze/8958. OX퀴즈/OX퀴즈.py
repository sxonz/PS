for i in range(int(input())):
    r = 0
    s = 0
    for j in input():
        if j == "O":
            s += 1
            r += s
        else:
            s = 0
    print(r)