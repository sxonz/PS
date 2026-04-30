def solution(num_list):
    a = num_list
    a.append(a[-1]-a[-2]) if a[-1] > a[-2] else a.append(a[-1]*2)
    return a