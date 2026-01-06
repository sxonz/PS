import sys
sys.setrecursionlimit(100000)
R,I = range,sys.stdin.readline
S = lambda:map(int,I().split())
log = 18
L = R(log-1,-1,-1)

node = int(I())
d = [[] for _ in R(node+1)]
for _ in R(node-1):
    a,b,w =S()
    d[a] += [(b,w)]
    d[b] += [(a,w)]

depth = [0]*(node+1)
nodeparents = [[1]*(log+1) for _ in R(node+1)]
nodedistance = [[0]*(log+1) for _ in R(node+1)]

visited = [False]*(node+1)
visited[1] = True
def dfs(current,w):
    for nextnode,cost in d[current]:
        if not visited[nextnode]:
            visited[nextnode] = True
            depth[nextnode] = w+1
            nodeparents[nextnode][0] = current
            nodedistance[nextnode][0] = cost
            dfs(nextnode,w+1)
dfs(1,0)

for k in R(1,log):
    for i in R(1,node+1):
        nodeparents[i][k] = nodeparents[nodeparents[i][k-1]][k-1]
        nodedistance[i][k] = nodedistance[i][k-1] + nodedistance[nodeparents[i][k-1]][k-1]


def lcanode(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    for i in L:
        if depth[b] - depth[a] >= 1<<i:
            b = nodeparents[b][i]
    if a == b:
        return a
    for i in L:
        if (A:=nodeparents[a][i]) != (B:=nodeparents[b][i]):
            a,b = A,B
    return nodeparents[a][0]

def lcadistance(a,b):
    cost = 0
    for k in L:
        if depth[a] < depth[nodeparents[b][k]]:
            cost += 1<<k
            b = nodeparents[b][k]
    return cost + (a!=b)

def query(orderedquery):
    querystyle = orderedquery[0]
    values = orderedquery[1:]

    if querystyle == 1:
        resultdistance = 0
        start,end = values[0],values[1]

        if depth[start] > depth[end]:
            start,end = end,start
        
        for currentlogvalue in L:
            if depth[start] <= depth[nodeparents[end][currentlogvalue]]:
                resultdistance += nodedistance[end][currentlogvalue]
                end = nodeparents[end][currentlogvalue]
        
        if start == end:
            return resultdistance
        else:
            for currentlogvalue in L:
                if nodeparents[start][currentlogvalue] != nodeparents[end][currentlogvalue]:
                    resultdistance += nodedistance[start][currentlogvalue]
                    resultdistance += nodedistance[end][currentlogvalue]
                    start = nodeparents[start][currentlogvalue]
                    end = nodeparents[end][currentlogvalue]
        return resultdistance + nodedistance[start][0] + nodedistance[end][0]
    
    else:
        start,end,kthdist = values[0],values[1],values[2]
        middlenode = lcanode(start,end)
        lcadist = lcadistance(middlenode,start)

        kthdist -= 1
        if lcadist == kthdist:
            return middlenode
        
        elif lcadist > kthdist:
            for currentlogvalue in L:
                if 1<<currentlogvalue <= kthdist:
                    kthdist -= 1<<currentlogvalue
                    start = nodeparents[start][currentlogvalue]
            return start
        
        else:
            kthdist -= lcadist
            reverselcadist = lcadistance(middlenode,end) - kthdist
            for currentlogvalue in L:
                if 1<<currentlogvalue <= reverselcadist:
                    reverselcadist -= 1<<currentlogvalue
                    end = nodeparents[end][currentlogvalue]
            return end

for _ in R(int(I())):
    print(query(list(S())))