n,m,k1,k2 = map(int,input().split())
d1 = [[] for i in range(n)]
d2 = [[] for i in range(n)]
for i in range(k1):
    a,b = map(int,input().split())
    d1[a-1].append(b-1)
for j in range(k2):
    a,b = map(int,input().split())
    d2[a-1].append(b-1)

connected = [-1]*m
def dfs(x,d):
    if visited[x]:
        return False
    visited[x] = True

    for nx in d[x]:
        if connected[nx] == -1 or dfs(connected[nx],d):
            connected[nx] = x
            return True
        
    return False
a1 = 0
a2 = 0
for i in range(n):
    visited = [False]*n
    a1 += dfs(i,d1)
connected = [-1]*m
for i in range(n):
    visited = [False]*n
    a2 += dfs(i,d2)

if a1 < a2:
    print("네 다음 힐딱이")
else:
    print("그만 알아보자")
