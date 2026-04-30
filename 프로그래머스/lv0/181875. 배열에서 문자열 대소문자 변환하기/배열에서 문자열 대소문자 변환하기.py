def solution(strArr):
    for i,j in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = j.lower()
        else:
            strArr[i] = j.upper()
    return strArr
        