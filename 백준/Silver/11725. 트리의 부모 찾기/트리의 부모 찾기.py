from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

x = 1
visited = [False]*(n+1)
queue = deque([x])
d = [[] for _ in range(n+1)]

while queue:
    x = queue.popleft()
    for i in tree[x]:
        if not visited[i]:
            visited [i] = True
            queue.append(i)
            d[i] = x
print(*d[2:],sep='\n')