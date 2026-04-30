def solution(strArr):
    slen = [0 for i in range(0,32)]
    for i in sorted(strArr,key=len):
        slen[len(i)] += 1
    return max(slen)