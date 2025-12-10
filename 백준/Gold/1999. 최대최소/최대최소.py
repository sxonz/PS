import sys
input = sys.stdin.readline

n,b,k = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
p = [[(0,0)]*(n-b+1) for i in range(n)]

for i in range(n):
    slide = d[i][:b]
    p[i][0] = (min(slide),max(slide))
    for j in range(b,n):
        slide.pop(0)
        slide.append(d[i][j])
        p[i][j-b+1] = (min(slide),max(slide))

for i in range(n-b+1):
    for j in range(n-b+1):
        p[i][j] = (min([p[k][j][0] for k in range(i,i+b)]), max([p[k][j][1] for k in range(i,i+b)]))
p = p[:n-b+1]

for i in range(k):
    x,y = map(int,input().split())
    print(p[x-1][y-1][1]-p[x-1][y-1][0])