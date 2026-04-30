def solution(park, routes):
    for i,j in enumerate(park):
        if j.count('S') == 1:
            start = [i,j.index('S')]
    W = len(park[0])
    current = start
    for i in routes:
        print(i)
        op,n = i.split()
        n = int(n)
        if op == 'E':
            if current[1] + n >= W: continue
            con = False
            for i in range(n):
                if park[current[0]][current[1] + i + 1] == 'X':
                    con = True
            if con == True:
                continue
            current = [current[0],current[1] + n]
        if op == 'W':
            con = False
            if current[1] - n < 0: continue
            for i in range(n):
                if park[current[0]][current[1] - i - 1] == 'X':
                    con = True
            if con == True:
                continue
            current = [current[0],current[1] - n]
        if op == 'N':
            con = False
            if current[0] - n < 0: continue
            for i in range(n):
                if park[current[0] - i - 1][current[1]] == 'X':
                    con = True
            if con == True:
                continue
            current = [current[0] - n,current[1]]
        if op == 'S':
            if current[0] + n >= len(park): continue
            con = False
            for i in range(n):
                if park[current[0] + i + 1][current[1]] == 'X':
                    con = True
            if con == True:
                continue
            current = [current[0] + n,current[1]]
    return current
            
            