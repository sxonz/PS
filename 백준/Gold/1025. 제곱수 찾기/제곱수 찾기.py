n,m = map(int,input().split())
d = [input() for i in range(n)]
ans = -1
for i in d:
    for j in "0149":
        if j in i:
            ans = max(ans,int(j))
for i in range(n):
    for j in range(m):
        for k in range(-n,n):
            for l in range(-m,m):
                if (k,l) == (0,0):
                    continue
                cur = ""
                x,y = i,j
                while 0<=x<n and 0<=y<m:
                    cur += d[x][y]
                    x,y = x+k,y+l
                    if int(int(cur)**0.5)**2 == int(cur):
                        ans = max(int(cur),ans)
print(ans)