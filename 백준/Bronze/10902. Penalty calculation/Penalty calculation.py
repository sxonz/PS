ans = 0
n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
f = -1
maxv = 0
for i in range(n):
    a,b = d[i]
    if b > maxv:
        maxv = b
        f = i
if d[f][1] == 0:
    p = 0
elif d[f][1] in [1,4]:
    p = d[f][0]+f*20
print(p)
