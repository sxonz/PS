ans = []
while True:
    n = int(input())
    if n == 0:
        break
    node = [tuple(map(int,input().split())) for i in range(n)]
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            edges.append((((node[i][0]-node[j][0])**2+(node[i][1]-node[j][1])**2)**0.5,i,j))
    edges.sort()
    parents = list(range(n+1))
    def F(x):
        if x != parents[x]:parents[x] = F(parents[x])
        return parents[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            parents[b] = a
        else:
            parents[a] = b
    m = int(1e10)
    for c,a,b in edges:
        if F(a) != F(b):
            U(a,b)
            m = c
        if F(0) == F(1):
            break
    ans.append((m))
    input()
for i,j in enumerate(ans):
    print(f"Scenario #{i+1}")
    j = round(j*1000)/1000
    j = str(j) + '0'*(4-len(str(j))+str(j).find('.'))
    print(f"Frog Distance = {j}\n")