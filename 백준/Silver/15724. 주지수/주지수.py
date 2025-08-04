n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
prefix_sum = [[0]*(m+1) for i in range(n+1)]


for i in range(1,n+1):
    for j in range(1,m+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + d[i-1][j-1]

for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(prefix_sum[c][d]-prefix_sum[a-1][d]-prefix_sum[c][b-1]+prefix_sum[a-1][b-1])