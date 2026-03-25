n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans = max(ans,d[i]-n+i)
print(ans)