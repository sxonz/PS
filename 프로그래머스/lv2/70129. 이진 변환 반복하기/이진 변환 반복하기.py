def solution(s):
    count = 0
    zerocount = 0
    while s != '1':
        zerocount += s.count('0')
        s = bin(len('1' * s.count('1'))).lstrip('0b')
        count += 1
    return [count,zerocount]