n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort(key=lambda x:x[1])
ans = int(1e9)
cur = 0
for a,b in d:
    cur += a
    tmp = b - cur
    if tmp<0:
        print(-1)
        break
    ans = min(ans,tmp)
else:
    print(ans)
