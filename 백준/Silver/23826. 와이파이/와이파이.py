n = int(input())
d = [tuple(map(int,input().split())) for i in range(n+1)]
val = [0]*(n+1)
for i in range(n+1):
    for j in range(i,n+1):
        val[j] += max(0,d[i][2]-abs(d[i][0]-d[j][0])-abs(d[i][1]-d[j][1]))*(-1)**(i>0)
        if i == j:
            continue
        val[i] += max(0,d[j][2]-abs(d[i][0]-d[j][0])-abs(d[i][1]-d[j][1]))*(-1)**(j>0)


val[0] = 0
if any(i > 0 for i in val):
    print(max(val))
else:
    print("IMPOSSIBLE")