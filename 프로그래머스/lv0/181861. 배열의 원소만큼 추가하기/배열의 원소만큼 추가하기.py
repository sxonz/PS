def solution(arr):
    ret = []
    for i in arr:
        for j in range(i):
            ret.append(i)
    return ret