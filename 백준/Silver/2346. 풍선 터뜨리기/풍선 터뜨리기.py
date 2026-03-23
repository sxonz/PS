from collections import deque
n = int(input())
d = list(map(int,input().split()))
d = deque([(i,j) for i,j in zip(d,range(1,n+1))])
ans = []
for i in range(n):
    tmp = d.popleft()
    if tmp[0] > 0:
        d.rotate(-tmp[0]+1)
    else:
        d.rotate(-tmp[0])
    ans.append(tmp[1])
print(*ans)
