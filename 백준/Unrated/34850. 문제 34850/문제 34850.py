x,y,p,a,b = map(int,input().split())
cur = (y-1)*b+p
res = 0
for i in range(x):
    res += cur
    cur -= a
print(res)