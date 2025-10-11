n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
ans = 0
s=e=-int(1e9)
for a,b in d:
    if a > e:
        ans += e-s
        s,e = a,b
    e = max(e,b)
ans += e-s
print(ans)
    
