n,k = map(int,input().split())
d = []
for i in range(n):
    a,b = map(int,input().split())
    s = list(map(int,input().split()))
    if b > a:
        d.append(1)
        continue
    s.sort()
    d.append(s[a-b])
d.sort()
cnt = 0
for i in d:
    if k >= i:
        k -= i
        cnt += 1
print(cnt)