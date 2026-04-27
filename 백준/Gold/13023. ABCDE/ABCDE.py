import sys

sys.setrecursionlimit(4000)

def dfs(x,tmp):
    flag = False
    if tmp == 4:
        return True
    
    for c in d[x]:
        if not visited[c]:
            break
    else:
        visited[x] = False
        return False
    
    for nx in d[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx,tmp+1):
                flag = True
                
    if not flag:
        visited[x] = False
        return False
    return True
            
    

n,m = map(int,input().split())
d = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)


for i in range(n):
    visited = [False] * (n+1)
    visited[i] = True
    if dfs(i,0):
        print(1)
        break
else:
    print(0)
