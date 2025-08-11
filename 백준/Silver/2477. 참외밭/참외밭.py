import sys
input = sys.stdin.readline

n = int(input())

d = [list(map(int, input().split())) for i in range(6)]

w = [0, 0]
h = [0, 0]
for i in range(6):
    if (d[i][0] <= 2) and (d[i][1] > w[1]):
        w = [i, d[i][1]]
    elif (d[i][0] in [3,4]) and (d[i][1] > h[1]):
        h = [i, d[i][1]]

print(n*(w[1]*h[1]-abs(d[(h[0]+1)%6][1]-d[(h[0]-1)%6][1])*abs(d[(w[0]-1)%6][1]-d[(w[0]+1)%6][1])))