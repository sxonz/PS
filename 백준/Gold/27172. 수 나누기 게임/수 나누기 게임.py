n = int(input())
d = list(map(int,input().split()))
check = set(d)
m = max(d)
point = [0]*1000001
for i in d:
    k = 2
    while i*k <= m:
        if i*k in check:
            point[i*k] -= 1
            point[i] += 1
        k += 1
for i in d:
    print(point[i],end=' ')