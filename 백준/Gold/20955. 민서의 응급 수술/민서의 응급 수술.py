n,m = map(int,input().split())
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
ans = 0
k = m
for i in range(m):
    a,b = map(int,input().split())
    a,b = F(a),F(b)
    if a == b:
        ans += 1
        k -= 1
    elif a<b:
        p[b] = a
    else:
        p[a] = b

print(ans + n-1-k)