n,k = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
ans = 0
for i in range(k):
    ans += i*d[i]
ans += sum(d[k:])*k
print(ans)