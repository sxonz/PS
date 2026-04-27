from collections import deque

testcase = int(input())

for t in range(testcase):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    time.insert(0,0)

    d = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    price = [0]*(n+1)
    queue = deque([])

    for _ in range(k):
        a,b = map(int,input().split())
        d[a].append(b)
        indegree[b] += 1

    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
        
    while queue:
        x = queue.popleft()

        for nx in d[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)
            price[nx] = max(price[nx],price[x]+time[x])
    w = int(input())
    print(price[w]+time[w])