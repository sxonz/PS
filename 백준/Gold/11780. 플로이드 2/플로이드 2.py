n = int(input())
m = int(input())
INF = int(1e12)
distance = [[INF]*(n+1) for i in range(n+1)]
path = [[i for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    distance[a][b] = min(distance[a][b],c)
    path[a][b] = b

for i in range(1,n+1):
    distance[i][i] = 0
    path[i][i] = []
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][k] == INF or distance[k][j] == INF or i == j:
                continue
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                path[i][j] = path[i][k]
for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] >= INF:
            distance[i][j] = 0
            path[i][j] = []
        print(distance[i][j],end=' ')
    print()
for x in range(1,n+1):
    for y in range(1,n+1):
        i,j = x,y
        if i == j or distance[i][j] == 0:
            print(0)
            continue
        ans = [i]
        while i!=j:
            ans.append(path[i][j])
            i = path[i][j]
        print(len(ans),*ans)