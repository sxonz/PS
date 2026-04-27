def ccw(p1,p2,p3):
    return (p2[0]-p1[0]) * (p3[1]-p2[1]) - (p2[1]-p1[1]) * (p3[0]-p2[0])
n = int(input())
d = []
for i in range(n):
    x,y,isin = input().split()
    if isin == "Y":
        d.append((int(x),int(y)))
d.sort()
ans = []
hull = [d[0],d[1]]
for i in d[2:]:
    while len(hull) >= 2 and ccw(hull[-2],hull[-1],i) < 0:
        hull.pop()
    hull.append(i)

ans += hull[:-1]

d = d[::-1]
hull = [d[0],d[1]]
for i in d[2:]:
    while len(hull) >= 2 and ccw(hull[-2],hull[-1],i) < 0:
        hull.pop()
    hull.append(i)

ans += hull[:-1]
print(len(ans))
for i in ans:
    print(*i)