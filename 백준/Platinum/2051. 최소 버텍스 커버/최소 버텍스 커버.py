I=lambda:map(int,input().split())
n,m = I()
R = range(1,n+1)
d = [[]]+[list(I())[1:] for i in R]

connected = [0]*(m+1)
def dfs(x,visited):
    if visited[x]:
        return 0
    visited[x] = 1
    for nx in d[x]:
        if not connected[nx] or dfs(connected[nx],visited):
            connected[nx] = x 
            return 1
    return 0

print(sum([dfs(i,[0]*(n+1)) for i in R]))

X = [set(),set()]
stack= [[i,1] for i in R if i not in connected]
while stack:
    x,cur = stack.pop()
    if cur and x not in X[0]:
        X[0].add(x)
        stack += [(nx,0)for nx in d[x]]
    elif((x in X[1])^1) and cur^1:
        X[1].add(x)
        stack.append((connected[x],1))

ra = set([connected[i] for i in range(1,m+1) if connected[i]])-X[0]
rb = set([i for i in range(1,m+1) if connected[i]])&X[1]

print(len(ra),*ra)
print(len(rb),*rb)