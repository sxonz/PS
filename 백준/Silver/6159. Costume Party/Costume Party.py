n,k = map(int,input().split())
d = [int(input()) for i in range(n)]
d.sort()
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if d[i]+d[j] <= k:
            ans += 1
        else:
            break
print(ans)