def solution(players, m, k):
    cnt = 0
    for i in range(len(players)):
        while players[i] >= m:
            for j in range(i,min(i+k,len(players))):
                players[j] -= m
            cnt += 1
    return cnt