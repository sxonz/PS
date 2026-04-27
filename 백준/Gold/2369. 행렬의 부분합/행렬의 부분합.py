n,m,mod = map(int,input().split())
d = [[0]+list(map(int,input().split())) for i in range(n)]
d = [[0]*(m+1)]+d
psum = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + d[i][j]
ans = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if psum[i][j] < mod:
            continue
        for k in range(1,i+1):
            for l in range(1,j+1):
                if (psum[i][j]-psum[k-1][j]-psum[i][l-1]+psum[k-1][l-1])%mod == 0:
                    ans += 1
print(ans)