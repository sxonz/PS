for t in range(int(input())):
    s = input().split()
    d = dict()
    for i in s:
        if i[0] not in d:
            d[i[0]] = 0
        d[i[0]] += 1
    r = list(d.keys())
    r.sort(key = lambda x:(-d[x],x))
    print(r[0])