from collections import deque

N = 400000
n,k = map(int,input().split())
dp = [-1]*N
dp[n] = 0
way = [0]*N
way[n] = 1
                                                                                                      
queue = deque([(n,0)])
while queue:
    x,w = queue.popleft()
    if x == k:
        break
    for i in 1,-1,x:
        nx = x+i
        if 0<=nx<N:
            if dp[nx] == -1 or dp[nx] == dp[x]+1:
                dp[nx] = dp[x] + 1
                if way[nx] == 0:
                    queue.append((nx,w+1))
                way[nx] += way[x]

print(dp[k])
print(way[k])