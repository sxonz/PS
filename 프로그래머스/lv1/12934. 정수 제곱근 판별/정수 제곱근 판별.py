def solution(n):
    for i in range(n):
        i += 1
        if i * i == n:
            return (i + 1) * (i + 1)
        if i == n:
            return -1