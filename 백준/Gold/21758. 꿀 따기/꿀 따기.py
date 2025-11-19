n = int(input())
d = list(map(int,input().split()))
ans = 0
for t in range(2):
    tmp = sum(d[2:])*2
    ans = max(ans,tmp)
    for i in range(2,n-1):
        tmp -= d[i]*2
        tmp += d[i-1]
        ans = max(ans,tmp)
    d.reverse()
ans = max(ans,sum(d[1:-1])+max(d[1:-1]))
print(ans)