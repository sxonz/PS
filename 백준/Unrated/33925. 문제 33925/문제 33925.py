n,j,s,h,k = map(int,input().split())
d = [input() for i in range(3)]
j1=j2=s1=0
for i in range(n):
    if d[0][i] == "v":
        s1 += 1
    if d[1][i] == "^":
        j2 += 1
    elif d[2][i] == "^":
        j1 += 1

live = 1
for i in range(j1):
    if j:
        j -= 1
    else:
        h -= k
    if h <= 0:
        live = 0
for i in range(j2):
    if j >= 2:
        j -= 2
    else:
        h -= k
    if h <= 0:
        live = 0
for i in range(s1):
    if s:
        s -= 1
    else:
        h -= k
    if h <= 0:
        live = 0

if live:
    print(h)
else:
    print(-1)
