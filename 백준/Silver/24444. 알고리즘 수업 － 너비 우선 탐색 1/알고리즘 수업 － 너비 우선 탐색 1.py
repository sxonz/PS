from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())

d = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a-=1; b-=1

    d[a].append(b)
    d[b].append(a)

for i in d:
    i.sort()

visit = [False]*(n)
visit[v-1] = True

answer = [0]*n
cnt = 1

queue = deque([v-1])

while queue:
    x = queue.popleft()
    answer[x] = cnt
    cnt += 1

    for nx in d[x]:
        if visit[nx] == False:
            visit[nx] = True
            queue.append(nx)

for i in answer:
    print(i)