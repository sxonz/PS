from itertools import combinations
n,m = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            house.append((i,j))
        elif d[i][j] == 2:
            chicken.append((i,j))
_min = int(1e9)
for comb in combinations(chicken,m):
    dist = 0
    for x,y in house:
        hdist = int(1e9)
        for cx,cy in comb:
            hdist = min(hdist,abs(cx-x)+abs(cy-y))
        dist += hdist
    _min = min(_min,dist)
print(_min)