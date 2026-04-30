from collections import deque
def solution(order):
    res = 0
    cur = 1
    m = 1
    subcon = deque([])
    for o in order:
        m = max(o,m)
        flag = False
        while cur < o:
            subcon.appendleft(cur)
            cur += 1
        if cur == o:
            res += 1
            cur += 1
            flag = True
            continue
        if cur > o:
            if subcon and subcon[0] == o:
                if m == cur:
                    cur += 1
                res += 1
                subcon.popleft()
                flag = True
        if not flag:
            break
    return res
        
            
            
        