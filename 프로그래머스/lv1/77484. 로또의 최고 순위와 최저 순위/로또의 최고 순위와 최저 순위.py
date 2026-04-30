def solution(lottos, win_nums):
    count = 0
    rcount = 6
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            count += 1
            rcount -= 1
        else:
            rcount -= 1
    if rcount == 0:
        rcount = 1
    if count == 0:
        count = 1
    return [7-count,7-rcount]