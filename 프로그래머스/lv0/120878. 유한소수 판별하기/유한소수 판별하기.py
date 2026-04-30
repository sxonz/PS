def solution(a, b):
    for i in [j for j in range(min(a,b),0,-1)]:
        if a % i == 0 and b % i == 0:
            a,b = a // i, b // i
    print(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2