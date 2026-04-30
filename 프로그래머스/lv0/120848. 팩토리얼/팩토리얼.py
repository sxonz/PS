def solution(n):
    sum = 1
    for i in range(1,n):
        sum *= i
        if sum > n:
            return i-1
    return n if n < 3 else 2