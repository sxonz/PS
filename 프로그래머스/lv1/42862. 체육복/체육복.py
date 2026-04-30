def solution(n, lost, reserve):
    lost = [0]+[i in lost for i in range(1,n+1)]
    reserve = [0]+[i in reserve for i in range(1,n+1)]
    for i in range(1,n+1):
        if lost[i] and reserve[i]:
            reserve[i] = False
            lost[i] = False
    for i in range(1,n+1):
        if not reserve[i]:
            continue
        if lost[i]:
            lost[i] = False
            continue
        if lost[i-1]:
            lost[i-1] = False
        elif i < n and lost[i+1]:
            lost[i+1] = False
    print(lost[1:])
    return lost[1:].count(False)
        
    