n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
outdegree = [0]*n
for i in range(n):
    for j in range(i+1,n):
        a = d[i][0]+d[j][0]*d[i][1]
        b = d[j][0]+d[i][0]*d[j][1]
        if a>b:
            outdegree[i] += 1
        else:
            outdegree[j] += 1

ans = sorted(range(1,n+1),key=lambda x:-outdegree[x-1])
print(*ans,sep='\n')