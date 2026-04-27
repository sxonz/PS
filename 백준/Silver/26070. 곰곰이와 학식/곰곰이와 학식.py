a = list(map(int,input().split()))
d = list(map(int,input().split()))
r = 0
for t in range(3):
    for i in range(3):
        a[i] -= d[i]
        r += d[i]
        d[i] = 0
        if a[i] < 0:
            r += a[i]
            d[i] = (-a[i])//3
            a[i] = 0
    d.insert(0,d.pop())


print(r)