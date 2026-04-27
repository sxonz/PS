n,m = map(int,input().split())
d = list(map(int,input().split()))
ans = 0
for i in range(len(d)-2):
    for j in range(i+1,len(d)-1):
        for k in range(j+1,len(d)):
            if d[i]+d[j]+d[k] > m:continue
            ans = max(ans,d[i]+d[j]+d[k])
print(ans)