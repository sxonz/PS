def solution(N, stages):
    p = [0]*N
    cur = 0
    for i in stages:
        if i <= N:
            p[i-1] += 1
        else:
            cur += 1
    d = []
    for idx,j in zip(range(N,0,-1),reversed(p)):
        print(idx,j)
        if j == 0:
            d.append((0,idx))
            continue
        cur += j
        d.append((-(j/cur),idx))
    d.sort()
    print(d)
    return [d[i][1] for i in range(N)]
        