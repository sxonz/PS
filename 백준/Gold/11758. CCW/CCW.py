p = [list(map(int,input().split())) for _ in range(3)]
tmp = p[0][0]*p[1][1]+p[1][0]*p[2][1]+p[2][0]*p[0][1]-p[0][1]*p[1][0]-p[1][1]*p[2][0]-p[2][1]*p[0][0]
if tmp == 0:
    print(0)
elif tmp > 0:
    print(1)
else:
    print(-1)