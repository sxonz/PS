def calculate(m, n, x, y):
    k = x
    while k <= m * n:
        if (k-x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1

for _ in range(int(input())):
    print(calculate(*map(int,input().split())))