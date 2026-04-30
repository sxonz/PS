def solution(n):
    answer = [[0]*n for i in range(n)]
    dir = ((0,1),(1,0),(0,-1),(-1,0))
    cd = 0
    cur = 1
    x,y = 0,0
    for i in range(n*n):
        answer[x][y] = cur
        cur += 1
        if not (0<=x+dir[cd][0]<n and 0<=y+dir[cd][1]<n and not answer[x+dir[cd][0]][y+dir[cd][1]]):
            cd = (cd + 1)%4
            
            
        x += dir[cd][0]
        y += dir[cd][1]
    
    return answer