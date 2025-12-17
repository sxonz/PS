for t in range(int(input())):
    a,b = input().split()
    if len(a) != len(b) or a.count("a") != b.count("a"):
        print(-1)
        continue

    n = len(a)
    p1,p2 = 0,0
    res = 0
    for i in range(a.count("a")):
        while a[p1] == "b":
            p1 += 1
        while b[p2] == "b":
            p2 += 1
        res += abs(p1-p2)
        p1 += 1
        p2 += 1
    print(res)