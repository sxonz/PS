from heapq import heappush,heappop
def solution(n,road,k):
    res = 0
    d = [[] for i in range(n+1)]
    for a,b,c in road:
        d[a].append((b,c))
        d[b].append((a,c))
    heap = [(0,1)]
    visited = [0]*(n+1)
    while heap:
        time,x = heappop(heap)
        if visited[x]:
            continue
        if time > k:
            return res
        res += 1
        visited[x] = 1
        for nx,cost in d[x]:
            if not visited[nx]:
                heappush(heap,(cost+time,nx))
    return res
                