from collections import deque

n, k = map(int, input().split())
queue = deque([n])
visited = [False]*200000
d = [0]*200000
visited[n] = True

x = -1
while x != k:
    x = queue.popleft()
    if 0<=x*2<200000 and not visited[x*2] :
        visited[x*2] = True
        d[2*x] = d[x]
        queue.appendleft(x*2)
    for i in (-1,1):
        if 0<=i+x<200000 and not visited[i+x]:
            visited[i+x] = True
            d[i+x] = d[x]+1
            queue.append(i+x)
print(d[k])