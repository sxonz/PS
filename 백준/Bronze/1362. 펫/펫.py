i = 0
while True:
    i += 1
    o,w = map(int,input().split())
    if (o,w) == (0,0):
        break
    flag = False
    while True:
        q,n = input().split()
        if q == "#":
            break
        if q == "F":
            w += int(n)
        else:
            w -= int(n)
            if w <= 0:
                flag = True
                
    if flag:
        print(f"{i} RIP")
    elif o/2 < w < o*2:
        print(f"{i} :-)")
    else:
        print(f"{i} :-(")