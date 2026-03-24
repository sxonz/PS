from collections import deque
queue = deque([])
for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    idx = {i:j for i,j in zip(d,range(n))}
    m = int(input())
    ch = [[0]*(n+1) for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        ch[idx[a]][idx[b]] = 1
        ch[idx[b]][idx[a]] = 1

    graph = [[] for i in range(n)]
    indegree = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            if ch[i][j]:
                graph[j].append(i)
                indegree[i] += 1
            else:
                graph[i].append(j)
                indegree[j] += 1

    queue = deque([])
    visited = [0]*n
    for i in range(n):
        if not indegree[i]:
            queue.append(i)
            visited[i] = 1

    flag = True
    ans = []
    while queue:
        x = queue.popleft()
        ans.append(d[x])
        for nx in graph[x]:
            if not visited[nx]:
                indegree[nx] -= 1
                if not indegree[nx]:
                    visited[nx] = 1
                    indegree[nx] = 0
                    queue.append(nx)
            else:
                flag = False
    if 0 in visited:
        flag = False

    if flag:
        print(*ans)
    else:
        print("IMPOSSIBLE")

    