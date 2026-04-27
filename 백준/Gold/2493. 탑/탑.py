n = int(input())
d = list(map(int,input().split()))
d.reverse()

ans = [0]*n
queue = []
for i in range(n):
    while queue and queue[-1][1] <= d[i]:
        tmp = queue.pop()
        ans[tmp[0]] = i
    queue.append((i,d[i]))
r = []
for i in reversed(ans):
    if i == 0:
        r.append(0)
    else:
        r.append(n-i)
print(' '.join([str(i) for i in r]))
