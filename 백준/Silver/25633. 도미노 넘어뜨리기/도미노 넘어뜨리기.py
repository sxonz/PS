n = int(input())
d = list(map(int,input().split()))
cnt = [0]*(n+1)
for i in range(n):
    for j in range(n-1,-1,-1):
        if cnt[j] >= d[i] or j == 0:
            cnt[j+1] = max(cnt[j+1],cnt[j]+d[i])
for i in range(n,-1,-1):
    if cnt[i]:
        print(i)
        break