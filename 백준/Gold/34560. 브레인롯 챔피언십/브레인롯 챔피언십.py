from collections import deque

n = int(input())
d = [input().split() for i in range(n)]

indegree = [0]*n
graph = [[] for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        a = 0
        b = 0
        for k in range(1,4):
            if int(d[i][k]) > int(d[j][k]):
                a += 1
            elif int(d[j][k]) > int(d[i][k]):
                b += 1
        if a > b:
            indegree[j] += 1
            graph[i].append(j)
        elif b > a:
            indegree[i] += 1
            graph[j].append(i)

if 0 not in indegree:
    print("Paradoxe Absurdo")
else:
    ans = []
    queue = deque([])
    cnt = n
    for i in range(n): 
        if indegree[i] == 0:
            ans.append(i)
            queue.append(i)
            cnt -= 1
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)
                cnt -= 1
    if cnt:
        print("Paradoxe Absurdo")
    else:
        for i in sorted(ans,key=lambda x:d[x][0]):
            print(d[i][0])