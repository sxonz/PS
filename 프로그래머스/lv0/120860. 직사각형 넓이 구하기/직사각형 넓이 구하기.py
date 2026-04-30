def solution(dots):
    W = [i[0] for i in dots]
    H = [i[1] for i in dots]
    return (max(W) - min(W)) * (max(H) - min(H))