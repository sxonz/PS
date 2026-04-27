n,m = map(int,input().split())
d = [list(input()) for i in range(n)]
w,v1,v2,vac,s,e = 0,0,0,0,0,0
for j in d:
    for i in j:
        if i == "#":
            w += 1
        elif i in "UDLR":
            v1 += 1
        elif i == "A":
            v2 += 1
        elif i == "V":
            vac += 1
        elif i == "S":
            s += 1
        elif i == "E":
            e += 1
if w <= 1 and v1 <= 1 and v2 == 0 and vac == 0 and e == 1 and s == 1:
    print(1)
elif v2 == 0 and vac == 0 and e == 1 and s == 1:
    print(2)
elif v2 == 0 and e == 1 and s == 1:
    print(3)
elif e == 1 and s == 1:
    print(4)
else:
    print(-1)
