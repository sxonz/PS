n = int(input())
d = list(map(int,input().split()))
s = sum(d)
cur = d[0]
v = int(input())
for t in range(int(input())):
    cur += v*cur/s
    s += v
print(cur)