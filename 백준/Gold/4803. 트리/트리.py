from collections import deque
import sys
I = lambda:map(int,sys.stdin.readline().split())
ans = []
while True:
    n,m = I()
    if not n+m:
        break
    d = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = I()
        d[a].append(b)
        d[b].append(a)
    queue = deque([])
    visited = [False]*(n+1)
    t = 0
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            isTree = True
            queue.append((i,i))
            while queue:
                fx,x = queue.popleft()
                for nx in d[x]:
                    if visited[nx]:
                        if fx-nx:
                            isTree = False
                    else:
                        visited[nx] = True
                        queue.append((x,nx))
            if isTree:
                t += 1
    ans.append(t)
idx = 1
for i in ans:
    if not i:
        print(f"Case {idx}: No trees.")
    elif i == 1:
        print(f"Case {idx}: There is one tree.")
    else:
        print(f"Case {idx}: A forest of {i} trees.")
    idx += 1
    