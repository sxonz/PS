from heapq import *
testcase = int(input())
ans = []
for test in range(testcase):
    n,m,s = map(int,input().split())
    d = [[] for i in range(n+1)]
    for i in range(m):
        a,b,c = map(int,input().split())
        d[b].append((a,c))
    
    heap = [(0,s)]
    time = [0]*(n+1)
    visited = [False]*(n+1)
    cnt = 0
    t = 0
    while heap:
        cost,x = heappop(heap)
        if visited[x]:
            continue
        visited[x] = True
        t = time[x] = cost

        cnt += 1
        for nx,c in d[x]:
            if not visited[nx]:
                heappush(heap,(cost+c,nx))
    print(cnt,t)