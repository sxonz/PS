testcase = int(input())
result = []
for test in range(testcase):
    n = int(input())
    edges = []
    for i in range(n):
        row = list(map(int,input().split()))
        for j in range(i+1,n):
            if row[j]:
                edges.append((i,j))
    parents = list(range(n+1))
    def Find(x):
        if x-parents[x]:parents[x] = Find(parents[x])
        return parents[x]
    def Union(a,b):
        a,b = Find(a),Find(b)
        if a<b:
            parents[b] = a
        else:
            parents[a] = b
    def Cycle(a,b):
        return Find(a) == Find(b)
    edgeCnt = 0
    for a,b in edges:
        if Cycle(a,b):
            continue
        Union(a,b)
        edgeCnt += 1
    result.append(edgeCnt)
for r in result:
    print(r)