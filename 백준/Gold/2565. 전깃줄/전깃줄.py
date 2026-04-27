n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
d = [i[1] for i in d]
dp = [0]*n
def lis(idx):
    s = dp[idx]
    if s:
        return s
    m = 0
    for i in range(idx+1,n):
        if d[i] > d[idx]:
            m = max(m, lis(i))
    dp[idx] = m+1
    return m+1
print(n-max([lis(i) for i in range(n)]))
