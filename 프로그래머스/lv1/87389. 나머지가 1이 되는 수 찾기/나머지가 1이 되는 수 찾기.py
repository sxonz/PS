def solution(n):
    for i in range(n):
        if i == 0:
            continue
        if n % i == 1:
            return i