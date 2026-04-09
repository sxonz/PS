n,m = map(int,input().split())
d = tuple(map(int,input().split()))
cur = 0
for i in range(m):
    r = int(input())
    if d[cur] <= r:
        cur ^= 1
print(d[cur])