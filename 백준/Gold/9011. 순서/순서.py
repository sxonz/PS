res = []
testcase = int(input())
for t in range(testcase):
    n = int(input())
    d = list(map(int,input().split()))
    d.reverse()
    r = list(range(1,n+1))
    s = []
    for i in d:
        if i >= len(r):
            res.append(["IMPOSSIBLE"])
            break
        s.append(r.pop(i))
    else:
        res.append(s[::-1])
for i in res:
    print(*i)