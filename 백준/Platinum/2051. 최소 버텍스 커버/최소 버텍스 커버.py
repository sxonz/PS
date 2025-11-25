from collections import deque

n,m = map(int,input().split())
d = [[]]
for i in range(n):
    t,*r = map(int,input().split())
    d.append(r)


connected = [0]*(m+1)
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    for nx in d[x]:
        if not connected[nx] or dfs(connected[nx]):
            connected[nx] = x
            return True
    
    return False

ans = 0
for i in range(1,n+1):
    visited = [False]*(n+1)
    ans += dfs(i)

a = set(range(1,n+1)) - set(connected)

ax = set()
bx = set()
queue = deque([[i,1] for i in a])
visb = [False]*(m+1)
while queue:
    x,cur = queue.popleft()
    if cur:
        ax.add(x)
        for nx in d[x]:
            if not visb[nx]:
                visb[nx] = True
                queue.append((nx,0))
    else:
        if x not in bx:
            bx.add(x)   
            queue.append((connected[x],1))

ra = set([connected[i] for i in range(1,m+1) if connected[i]])-ax
rb = set([i for i in range(1,m+1) if connected[i]])&bx
print(ans)
print(len(ra),*ra)
print(len(rb),*rb)