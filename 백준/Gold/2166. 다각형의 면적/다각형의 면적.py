n = int(input())
dot = [list(map(int,input().split())) for _ in range(n)]
dot.append(dot[0])
p,m = 0,0
for i in range(n):
    p += dot[i][0]*dot[i+1][1]
    m += dot[i][1]*dot[i+1][0]

S = abs(p-m)/2
print(round(S,1))