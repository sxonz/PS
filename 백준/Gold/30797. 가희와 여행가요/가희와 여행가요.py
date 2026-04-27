import sys
sys.setrecursionlimit(100000)
I = lambda: map(int, input().split())
n, m = I()
edges = []
for _ in range(m):
    a, b, c, t = I()
    edges.append((c, t, a, b))

edges.sort()

p = list(range(n + 1))

def f(x):
    if x != p[x]:  
        p[x] = f(p[x])  
    return p[x]

def union(a, b):
    a, b = f(a), f(b)
    if a != b:
        p[b] = a  

cost = 0
time = 0
cnt = 0  

for c, t, a, b in edges:
    if f(a) != f(b):
        union(a, b)
        cost += c
        time = max(time, t)
        cnt += 1

if cnt == n - 1:
    print(time, cost)
else:
    print(-1)