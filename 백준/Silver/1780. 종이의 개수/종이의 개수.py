n = int(input())

d = [list(map(int,input().split())) for _ in range(n)]
def f(size,idx):
    x,y = idx
    temp = [0,0,0]
    if size == 1:
        temp[d[x][y]] += 1
        return temp
    
    for i in range(3):
        for j in range(3):
            ns = size//3
            nx,ny = x+i*ns,y+j*ns
            t = f(ns,(nx,ny))
            temp = [k+l for k,l in zip(t,temp)]
    if max(temp) == 9 and sum(temp) == 9:
        temp = [0,0,0]
        temp[d[x][y]] += 1
    return temp
    
tmp = f(n,(0,0))
for i in range(-1,2):
    print(tmp[i])