d = list(map(int,input().split()))
d.sort()
print(d[0]+d[1]+min(d[2],d[0]+d[1]-1))