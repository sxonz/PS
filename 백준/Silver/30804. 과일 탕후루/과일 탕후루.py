n = int(input())
d = list(map(int,input().split()))
m = 1
for i in range(1,9):
    for j in range(i+1,10):
        tmp = d[::]
        dp = [0]*n
        dp[0] = 1
        if tmp[0] == i:
            tmp[0] = j
        for k in range(1,n):
            if tmp[k] == i:
                tmp[k] = j
            r = (tmp[k-1] == tmp[k]) * dp[k-1] + 1
            dp[k] = r
            m = max(m,r)
print(m)