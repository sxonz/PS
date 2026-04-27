m,n = map(int,input().split())
d = [input().split() for i in range(n)]
dp = dict()
def bitcoin(x,y):
    if x<0 or y<0:return 0
    if x == 0 and y == 0:
        return 1
    if d[x][y] == '0':
        return 0
    if (x,y)in dp:return dp[(x,y)]
    dp[(x,y)] = bitcoin(x-1,y) | bitcoin(x,y-1)
    return dp[(x,y)]

print("YNeos"[bitcoin(n-1,m-1)^1::2])