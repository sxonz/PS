n = int(input())
d = list(map(int,input().split()))
d.sort()
vis =[0]*n
for _ in range(2):
    bef = -1
    for i in range(n):
        if bef<d[i] and not vis[i]:
            vis[i] = 1
            bef = d[i]
print(sum(vis))