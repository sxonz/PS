n,k,r = map(int,input().split())
d = [list(map(int,input().split()))[1:] for i in range(n)]
score = list(map(int,input().split()))
idx = list(range(n))
idx.sort(key=lambda x:-score[x])

connected = [[] for i in range(k+1)]
def dfs(x):
    if visited[x]:
        return 0
    visited[x] = 1
    for nx in d[x]:
        if len(connected[nx]) < r:
            connected[nx].append(x)
            return True
        for i in range(r):
            if dfs(connected[nx][i]):
                connected[nx][i] = x
                return True
    
    return False

for i in range(n):
    visited = [0]*n
    dfs(idx[i])
for i in connected[1:]:
    print(len(i),*[j+1 for j in i])