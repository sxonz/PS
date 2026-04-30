def solution(s):
    s = s.split()
    min = 99999
    max = -99999
    for i in s:
        i = int(i)
        if i < min:
            min = i
        if i > max:
            max = i
    return str(min) + ' ' + str(max)