def solution(d, budget):
    d = sorted(d)
    print(d)
    cnt = 0
    for i in d:
        if budget < i:
            break
        else:
            budget -= i
            cnt += 1
    return cnt
        