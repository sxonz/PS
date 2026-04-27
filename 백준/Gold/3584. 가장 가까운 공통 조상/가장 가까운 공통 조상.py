import sys
sys.setrecursionlimit(100000)
testcase = int(input())
ans = []
for test in range(testcase):

    n = int(input())
    d = [[] for i in range(n+1)]
    parents = list(range(n+1))
    depth = [0]*(n+1)

    for i in range(n-1):
        a,b = map(int,input().split())
        d[a].append(b)
        parents[b] = a

    for i in range(1,n+1):
        if parents[i] == i:
            r = i

    def dfs(x):
        for nx in d[x]:
            depth[nx] = depth[x] + 1
            dfs(nx)
    depth[r] = 1
    dfs(r)

    s,e = map(int,input().split())
    while depth[s] != depth[e]:
        if depth[s] < depth[e]:
            e = parents[e]
        else:
            s = parents[s]
    while s != e:
        s = parents[s]
        e = parents[e]
    ans.append(s)
for i in ans:
    print(i)