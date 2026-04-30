from collections import deque
def solution(n, wires):
    d = [[] for _ in range(n+1)]
    ans = []
    for a,b in wires:
        d[a].append(b)
        d[b].append(a)
    for i in range(1,n+1):
        visited = [False]*(n+1)
        visited[i] = True
        cnt = [0]
        queue = deque([])
        for x in d[i]:
            queue.append(x)
            visited[x] = True
            cur = 0
            while queue:
                cx = queue.popleft()
                cur += 1
                for nx in d[cx]:
                    if not visited[nx]:
                        visited[nx] = True
                        queue.append(nx)
            cnt.append(cur)
        for c in cnt:
            ans.append(abs(c+c-n))
    return min(ans)
                
        