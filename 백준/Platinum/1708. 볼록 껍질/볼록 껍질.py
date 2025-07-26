def ccw(p1,p2,p3):
    return (p2[0]-p1[0]) * (p3[1]-p2[1]) - (p3[0] - p2[0]) * (p2[1]-p1[1])

n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]

d.sort()

ans = 0
for i in range(2):
    s = [d[0],d[1]]

    for j in d[2:]:
        while len(s) >= 2 and ccw(s[-2],s[-1],j) >= 0:
            s.pop()
        s.append(j)
    ans += len(s)
    d = d[::-1]
print(ans - 2)