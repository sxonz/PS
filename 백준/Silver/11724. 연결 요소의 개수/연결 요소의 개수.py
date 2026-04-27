from collections import deque

n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False] * (n+1)
queue = deque([])

def bfs():

    while queue:
        c = queue.popleft()

        for i in d[c]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

cnt = 0

for node in range(1,n+1):
    if not visited[node]:
        queue.append(node)
        bfs()
        cnt += 1
print(cnt)