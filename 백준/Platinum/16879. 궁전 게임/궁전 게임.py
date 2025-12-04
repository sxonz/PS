import sys
input = sys.stdin.readline

maxsize = 3072
r = [[0,1,2],[1,2,0],[2,0,1]]
def dnc(size,x,y,snum):
    if size == 3:
        return snum + r[x][y]
    elif (x<size//2) ^ (y<size//2):
        return dnc(size//2,x%(size//2),y%(size//2),snum + size//2)
    else:
        return dnc(size//2,x%(size//2),y%(size//2),snum)

n = int(input())
res = 0
for i in range(n):
    x,y = map(int,input().split())
    res ^= dnc(maxsize,x,y,0)
if not res:
    print("cubelover")
else:
    print("koosaga")