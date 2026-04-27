dx,dy = (-1,1,0,0),(0,0,-1,1)
flag = False

r,c = map(int,input().split())
d = [list(input().replace('.','D')) for _ in range(r)]
for i in range(r):
    if flag:
          break
    for j in range(c):
        if flag:
              break
        if d[i][j] == 'W':
            for x in range(4):
                ni,nj = i+dx[x],j+dy[x]
                if (0<=ni<r and 0<=nj<c):
                   if d[ni][nj] == 'S':
                       flag = True
                       print(0)
                       break
else:
     print(1)
     for i in range(r):
          print(''.join(d[i]))
          
          
            