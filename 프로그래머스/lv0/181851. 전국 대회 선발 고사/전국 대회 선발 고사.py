def solution(rank, attendance):
    r = [rank.index(i+1) for i in range(len(rank)) if attendance[rank.index(i+1)]]
    return r[0]*10000 + r[1]*100 + r[2]