def f(x):
    r = 0
    while x:
        r += x%10
        x //= 10
    return r

while True:
    n = int(input())
    if not n:
        break
    while n>9:
        n = f(n)
    print(n)