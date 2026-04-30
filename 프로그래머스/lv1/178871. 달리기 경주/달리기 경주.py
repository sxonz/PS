def solution(players, callings):
    p = {}
    for i,j in enumerate(players):
        p[j] = i
    for i in callings:
        p1,p2 = p[i]-1, p[i]
        p[players[p1]] = p2
        p[players[p2]] = p1
        players[p1],players[p2] = players[p2],players[p1]
        
    return players