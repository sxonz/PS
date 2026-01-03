import sys
sys.setrecursionlimit(100000)
n = int(input())
d = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
cost = list(map(int,input().split()))
def dfs(x):
    subtree = 0
    for nx in d[x]:
        subtree += dfs(nx)
    return max(subtree+cost[x],0)
if not (r := dfs(0)):
    print(cost[0])
else:
    print(r)

