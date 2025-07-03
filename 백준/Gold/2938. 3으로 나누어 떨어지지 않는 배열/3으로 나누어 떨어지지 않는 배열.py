n = int(input())
d = list(map(int,input().split()))
m = [[],[],[]]

for i in d:
    m[i%3].append(i)

if len(m[0]) >= (n+3)//2:
    print(-1)
elif len(m[0]) == 0:
    if (len(m[1]) == 0 or len(m[2]) == 0):
        print(*d)
    else:
        print(-1)
else:
    res = []
    t = m[0].pop()
    for i in m[1]:
        if m[0]:
            res.append(m[0].pop())
        res.append(i)
    res.append(t)
    for i in m[2]:
        res.append(i)
        if m[0]:
            res.append(m[0].pop())
    print(*res)