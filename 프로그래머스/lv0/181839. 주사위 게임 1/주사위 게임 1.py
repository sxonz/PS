def solution(a, b):
    if (a+b) % 2 == 0:
        return a**2 + b**2 if a % 2 != 0 else abs(a-b)
    return (a+b) * 2 