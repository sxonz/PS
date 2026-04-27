from collections import deque
dx,dy,T,t,r=(-1,1,0,0),(0,0,-1,1),True,input,range
for _ in r(int(t())):
    m,n=map(int,t().split());d,s,e=[list(t()) for i in r(m)],(0,0),[]
    for i in r(m):
        for j in r(n):
            if d[i][j]=='S':s=(i,j)
            if d[i][j]=='G':e.append((i,j))
    q,v,c=deque([s]),[[False]*n for i in r(m)],[[0]*n for i in r(m)];v[s[0]][s[1]]=T
    while q:
        x,y = q.popleft()
        if (x,y) in e:print('Shortest Path: {0}'.format(c[x][y]));break
        for i in r(4):
            k,u=x+dx[i],y+dy[i]
            if 0<=k<n and 0<=u<m and d[k][u] != 'X' and not v[k][u]:v[k][u],c[k][u]=T,c[x][y]+1;q.append((k,u))
    else:print('No Exit')