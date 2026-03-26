for t in range(int(input())):
    n,m,k = map(int,input().split())
    d = input().split()
    ans = 0
    r = dict()
    for i in range(n):
        if d[i][-k:] not in r:
            r[d[i][-k:]] = 0
        r[d[i][-k:]] += 1
    print(sum([r[i]//2 for i in r]))