import sys
I = lambda:map(int,sys.stdin.readline().split())
n,m = I()
tmp = []
for _ in range(m):
    a,b = I()
    tmp.append((a,b))
s,e,k = I()
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b = F(a),F(b)
    if b != e and a<b:
        p[b] = a
    else:
        p[a] = b
for a,b in tmp:
    if F(a)!=F(b):
        U(a,b)
cnt = {}

ans = 0
pt = [F(i) for i in range(1,n+1)]
for i in range(n):
    if pt[i] == e:
        continue
    if pt[i] == s:
        ans += 1
        continue
    if pt[i] not in cnt:
        cnt[pt[i]] = 1
    else:
        cnt[pt[i]] += 1
res = list(cnt.values())
res.sort(reverse=True)
print(ans+sum(res[:k]))
