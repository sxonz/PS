from collections import deque
n = int(input())
queue = deque([])
a = []
b = []
c = []
for i in range(n):
    query,*r = map(int,input().split())
    if query == 1:
        queue.append(r)
    else:
        p,m = queue.popleft()
        if m == r[0]:
            a.append(p)
        else:
            b.append(p)
for p,m in queue:
    c.append(p)
for i in [a,b,c]:
    if i:
        print(*sorted(i))
    else:
        print(None)