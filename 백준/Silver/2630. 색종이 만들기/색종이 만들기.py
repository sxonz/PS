n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

def f(size,idx):
    x,y = idx
    temp = [0,0]
    if size == 1:
        temp[d[x][y]] += 1
        return temp
    for i in range(2):
        for j in range(2):
            ns = size // 2
            nx,ny = x+i*ns,y+j*ns
            t = f(ns,(nx,ny))
            temp = [j+k for j,k in zip(t,temp)]
    if max(temp) == sum(temp):
        temp = [0,0]
        temp[d[x][y]] += 1
    return temp

tmp = f(n,(0,0))
print(tmp[0])
print(tmp[1])