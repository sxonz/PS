n = int(input())
d = list(map(int,input().split()))
ans = [-1]*(n)

queue = []
for i in range(n):
    while queue and queue[-1][1] < d[i]:
        tmp = queue.pop()
        ans[tmp[0]] = d[i]
    queue.append((i,d[i]))
print(*ans)