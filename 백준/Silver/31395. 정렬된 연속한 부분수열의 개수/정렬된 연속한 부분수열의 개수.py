n = int(input())
d = list(map(int,input().split()))
r = [1]*n
for i in range(1,n):
    if d[i-1] < d[i]:
        r[i] = r[i-1] + 1
ans = 0
for i in range(1,n):
    if r[i] == 1:
        ans += (r[i-1]*(r[i-1]-1)) // 2
print(ans + (r[-1] * (r[-1]-1) // 2) + n)