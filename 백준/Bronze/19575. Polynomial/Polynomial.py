import sys
input = sys.stdin.readline

n,x = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n+1)]
d.reverse()
ans = 0
cur = 1
MOD = int(1e9)+7
for a,b in d:
    ans = (ans + a*cur)%MOD
    cur *= x
    cur %= MOD

print(ans)