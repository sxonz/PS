from collections import deque

n,k = map(int, input().split())
d = deque(range(1,n+1))

res = []
while d:
    for _ in range(k-1):
        d.append(d.popleft())
    res.append(str(d.popleft()))

print('<'+', '.join(res)+'>')