n,m = map(int,input().split())
d = [list(map(int,input().split()))[::-1] for i in range(n)]
d = list(sorted(zip(d,range(n)),reverse=True))
def sdist(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2
ans = 0
flag = False
for i in range(m):
    x,y = map(int,input().split())
    if flag:
        flag = False
        continue
    for tmp,num in d:
        _,r,y2,x2 = tmp
        if sdist(x,y,x2,y2) <= r**2:
            if num == 0:
                ans += 1
            flag = False
            break
    else:
        flag = True
    
print(ans)