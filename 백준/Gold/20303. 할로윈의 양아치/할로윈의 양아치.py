import sys
I = lambda:map(int,input().split())
n,m,k = I()
c = list(I())
p = [0]+[-i for i in c]
def F(x):
    if p[x]<0:return x
    p[x] = F(p[x])
    return p[x]
def U(a,b):
    a,b=F(a),F(b)
    if a<b:
        p[a] += p[b]
        p[b] = a
    else:
        p[b] += p[a]
        p[a] = b
for i in range(m):
    a,b = I()
    if F(a)-F(b):
        U(a,b)
candy = dict()
for i in range(1,n+1):
    j = F(i)
    if p[i] < 0:
        if i not in candy:
            candy[j] = [1,-p[j]]
        else:
            candy[j][0] += 1
            candy[j][1] = -p[j]
    else:
        if j not in candy:
            candy[j] = [1,0]
        else:
            candy[j][0] += 1
d = list(candy.values())
r = len(d)
dp = [[0]*(k) for _ in range(r)]
for i in range(r):
    for j in range(k):
        if j-d[i][0] >= 0:
            dp[i][j] = dp[i-1][j-d[i][0]] + d[i][1]
        dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i][j-1])
print(max(dp[-1]))