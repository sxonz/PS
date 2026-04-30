def solution(m, n, puddles):
    map = [[1 for i in range(m)] for j in range(n)]
    for i in puddles:
        map[i[1]-1][i[0]-1] = 0
        if i[0]-1 == 0:
            for j in range(i[1]-1,n):
                map[j][i[0]-1] = 0
        if i[1]-1 == 0:
            for j in range(i[0]-1,m):
                map[i[1]-1][j] = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                continue
            map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007 if map[i][j] != 0 else 0
    return map[n-1][m-1] % 1000000007
