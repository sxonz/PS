n = int(input())
d = list(map(int,input().split()))
d.sort()
ans = 0
MOD = 1000000007
cur = 1
for i in range(n):
    ans = (ans+cur*(d[i]-d[n-i-1]))%MOD
    cur = (cur*2)%MOD
print(ans)