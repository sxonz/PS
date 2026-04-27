import sys
input = sys.stdin.readline
M = 1000001
d = [i for i in range(M)]
for i in range(1,M//2+2):
    k = 2
    while i*k < M:
        d[i*k] += i
        k += 1
g = [d[0]]
for i in range(1,M):
    g.append(g[-1]+d[i])
for _ in range(int(input())):
    print(g[int(input())])
