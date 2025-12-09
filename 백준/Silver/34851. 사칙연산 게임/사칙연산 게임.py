MOD = 1000000007
n = int(input())
d = list(map(int,input().split()))
res = d[0]
cur = d[0]
for i in d[1:]:
    if cur <= 1 or i <= 1:
        res = (res+i)%MOD
        if cur+i < MOD:
            cur += i
    else:
        res = (res*i)%MOD
        if cur*i < MOD:
            cur *= i
print(res)
