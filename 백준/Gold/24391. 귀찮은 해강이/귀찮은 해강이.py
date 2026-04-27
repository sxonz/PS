n,m = map(int,input().split())
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]

for i in range(m):
    a,b = map(int,input().split())
    a,b = F(a),F(b)
    if a-b:
        if a<b:
            p[b] = a
        else:
            p[a] = b
d = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    if F(d[i]) - F(d[i+1]):
        ans += 1
print(ans) 