testcase = int(input())
ans = []
for test in range(testcase):
    n,r = map(int,input().split())
    s = input()
    dp = [-1]*n
    dp[0] = 0
    for i in range(1,n):
        m = int(1e9)
        for j in range(max(0,i-r-1),i):
            if s[j] == '.':
                m = min(m,dp[j])
        if m == int(1e9):
            dp[n-1] = 0
            break
        dp[i] = m + 1
    ans.append((test+1,n,r,s,dp[n-1]))
for t,n,m,s,d in ans:
    print(f'Day #{t}')
    print(n,m)
    print(s)
    print(d)
    print()
