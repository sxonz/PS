from itertools import combinations

n,m = map(int,input().split())
r = list(map(int,input().split()))
d = [list(map(int,input().split())) for i in range(n)]
maxv = max([sum([j==k for j,k in zip(r,i)]) for i in d])

for k in range(3,n+1,2):
    for i in combinations(range(n),k):
        cur = [0]*m
        for j in i:
            for l in range(m):
                cur[l] += d[j][l]
        cur = [j>k//2 for j in cur]
        if sum([x==y for x,y in zip(r,cur)]) > maxv:
            print(1)
            exit()
print(0)