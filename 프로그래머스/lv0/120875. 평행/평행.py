def solution(dots):
    angle = dict()
    for i in range(4):
        for j in range(i+1,4):
            a = abs(dots[i][1] - dots[j][1]) / abs(dots[i][0] - dots[j][0])
            if a not in angle:
                angle[a] = [[i,j]]
            else:
                angle[a].append([i,j])
    for i in angle:
        if len(angle[i]) >= 2:
            for j in range(len(angle[i])):
                for k in range(j+1,len(angle[i])):
                    if len(set([angle[i][j][0],angle[i][j][1],angle[i][k][0],angle[i][k][1]])) == 4:
                        return 1
    return 0