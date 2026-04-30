def solution(n,a,b):
    i = 0
    while True:
        if a == b:
             return i
        a = a // 2 if a % 2 == 0 else (a+1) // 2
        b = b // 2 if b % 2 == 0 else (b+1) // 2
        i += 1