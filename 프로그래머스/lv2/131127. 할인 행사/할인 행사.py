def solution(want, number, discount):
    cnt = 0
    want2 = []
    for i,j in zip(want,number):
        for k in range(j):
            want2.append(i)
    want2.sort()
    for i,j in enumerate(discount):
        temp = discount[i:i+10]
        if sorted(temp) == want2:
            cnt += 1
    return cnt