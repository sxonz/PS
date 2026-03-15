n = int(input())
t = list(map(int,input().split()))
d = {}
for i in t:
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1

ans = [-1]*(n)

queue = []
for i in range(n):
    while queue and d[queue[-1][1]] < d[t[i]]:
        tmp = queue.pop()
        ans[tmp[0]] = t[i]
    queue.append((i,t[i]))
print(*ans)