import sys
input = sys.stdin.readline
from collections import deque, defaultdict
 
testcase = int(input())
for _ in range(testcase):
    K, M, P = map(int, input().split())
    indegree = [[0, 0, 0] for _ in range(M+1)]
    ndict = defaultdict(list)
    for _ in range(P):
        s, e = map(int, input().split())
        ndict[s].append(e)
        indegree[e][0] += 1

    queue = deque()
    for i in range(1, M+1):
        if indegree[i][0] == 0:
            queue.append(i)
            indegree[i][1] = 1
 
    while queue:

        x = queue.popleft()

        for i in ndict[x]:
            indegree[i][0] -= 1

            if indegree[i][1] < indegree[x][1]:
                indegree[i][1] = indegree[x][1]
                indegree[i][2] = 1
            elif indegree[i][1] == indegree[x][1]:
                indegree[i][2] += 1

            if indegree[i][0] == 0:
                if indegree[i][2] > 1:
                    indegree[i][1] += 1
                queue.append(i)
 
    print(K, indegree[M][1])