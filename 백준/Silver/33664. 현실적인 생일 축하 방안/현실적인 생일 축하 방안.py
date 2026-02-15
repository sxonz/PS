b,n,m = map(int,input().split())
d = dict()
for i in range(n):
    name,p = input().split()
    d[name] = int(p)

ans = 0
for i in range(m):
    ans += d[input()]
print("un"*(ans > b)+"acceptable")