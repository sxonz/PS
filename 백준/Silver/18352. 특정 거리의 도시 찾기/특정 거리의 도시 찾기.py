from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
d = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)

queue = deque([x])
visited = [False] * (n + 1)
distance = [-1] * (n + 1)
visited[x], distance[x] = True, 0

while queue:
    cur = queue.popleft()
    for i in d[cur]:
        if not visited[i]:
            visited[i] = True
            distance[i] = distance[cur] + 1
            queue.append(i)

result = [i for i in range(1, n + 1) if distance[i] == k]
print("\n".join(map(str, sorted(result))) if result else -1)


