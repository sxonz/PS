while True:
    n = int(input())
    if n == 0:
        break
    m = 1
    while n != 1:
        m = max(n,m)
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1
    print(m)