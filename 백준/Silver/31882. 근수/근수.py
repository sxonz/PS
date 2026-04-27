n = int(input())
s = input()
d = [0]*(1000001)
cur = 0
for i in s:
    if i == '2':
        cur += 1
    elif cur != 0:
        d[cur] += 1
        cur = 0
if cur != 0:
    d[cur] += 1
dp = [1,1]
cur = 3
for i in range(2,1000001):
    dp.append(dp[-1]+cur)
    cur += i+1

res = 0
for i in range(1000001):
    if d[i] != 0:
        res += dp[i] *d[i]
print(res)