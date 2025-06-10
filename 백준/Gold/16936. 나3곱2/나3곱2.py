n = int(input())
d = list(map(int,input().split()))
r = []
for i in range(n):
    cur = d[i]
    a,b = 0,0
    while cur%2==0:
        cur //= 2
        a += 1
    while cur%3==0:
        cur //= 3
        b += 1
    offset = cur
    r.append((a,b))
r.sort(key = lambda x:(-x[1],x[0]))
print(*[offset * pow(2,i[0]) * pow(3,i[1]) for i in r])
