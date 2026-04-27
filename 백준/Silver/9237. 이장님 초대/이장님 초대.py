n = int(input())
d = list(map(int,input().split()))
d.sort(reverse=True)
ans = 0
for i in range(n):
    ans = max(ans,2+i+d[i])
print(ans)