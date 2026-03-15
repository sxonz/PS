from collections import deque

n,m = map(int,input().split())
if n:
    d = list(map(int,input().split()))
else:
    d = []

MAX = 20001
offset = 10000
dist = [0]*MAX
vis = [0]*MAX
vis[offset] = 1
queue = deque([0])
while queue:
    x = queue.popleft()
    for i in d:
        nx = i+x
        if 0 <= nx+offset < MAX:
            if not vis[nx+offset]:
                vis[nx+offset] = 1
                dist[nx+offset] = dist[x+offset]+1
                queue.append(nx)

print(dist[m+offset] if vis[m+offset] else -1)