from heapq import *
n = int(input())
d = [[] for i in range(n+1)]
time = []
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    c = tmp[0]
    m = tmp[1]
    time.append(c)
    for j in range(2,m+2):
        d[i].append((tmp[j],c))
heap = [(0,1)]
cnt = n
distance = [0]*(n+1)
o = False
while heap:
    cost,x = heappop(heap)
    if distance[x] or (x==1 and o):
        continue
    if x == 1:o = True
    distance[x] = cost
    cnt -= 1
    for nx,c in d[x]:
        heappush(heap,(cost+c,nx))
    if cnt == 0:
        cost += time[x-1]
print(cost)