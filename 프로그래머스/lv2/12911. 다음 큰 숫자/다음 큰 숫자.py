def solution(n):
    b = bin(n).count('1')
    for i in range(n+1,1000000):
        if b == bin(i).count('1'):
            return i