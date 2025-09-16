n = int(input())
m = int(input())
INF = int(1e9)
distance = [[INF]*n for i in range(n)]
for i in range(m):
    a,b,w = map(int,input().split())
    a -= 1
    b -= 1
    distance[a][b] = min(distance[a][b],w)
for i in range(n):
    distance[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            distance[i][j] = 0

for i in distance:
    print(*i)
