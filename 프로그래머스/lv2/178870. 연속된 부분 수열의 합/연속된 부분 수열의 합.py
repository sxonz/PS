def solution(s, k):
    n = len(s)
    prefix_sum = [0]
    for i in s:
        prefix_sum += [i+prefix_sum[-1]]
    p1,p2 = 0,1
    ans = int(1e8)
    r = [0,0]
    while p1 < n and p2<=n:
        tmp = prefix_sum[p2] - prefix_sum[p1]
        if tmp == k:
            if ans>p2-p1:
                ans = p2-p1
                r = [p1,p2-1]
            p2 += 1
        elif tmp < k:
            p2 += 1
        else:
            p1 += 1
    return r