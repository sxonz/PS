import sys
input = sys.stdin.readline
m,n = map(int,input().split())
d = [list(map(int,input().strip())) for _ in range(m)]
save = [[0] * (n+2) for _ in range(m+2)]
output = [[0] * (n+2) for _ in range(m+2)]
for i in range(1,m+1):
    output[i][1] = d[i-1][0]
result = 0
for j in range(1,n+1):
    for i in range(1,m+1):
        save[i][j] = max(output[i-1][j-1],output[i][j-1],output[i+1][j-1])
        output[i][j] = save[i][j] + d[i-1][j-1]
        result = max(save[i][j],result)
print(result)