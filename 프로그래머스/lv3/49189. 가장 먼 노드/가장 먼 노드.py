from collections import deque


def solution(n, edge):
    d = [[] for _ in range(n+1)]
    for a,b in edge:
        d[a].append(b)
        d[b].append(a)
        
    queue = deque([1])
    visited = [False]*(n+1)
    visited[1] = True
    distance = [-1] * (n+1)
    distance[1] = 0
    
    while queue:
        x = queue.popleft()
        for nx in d[x]:
            if not visited[nx]:
                visited[nx] = True
                distance[nx] = distance[x] +1
                queue.append(nx)
    m = max(distance)
    
    cnt = 0
    for d in distance:
        if d == m:
            cnt += 1
    return cnt