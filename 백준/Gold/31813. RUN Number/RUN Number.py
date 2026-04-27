testcase = int(input())
for test in range(testcase):
    k,n = map(int,input().split())
    dec = int("1"*k)
    cur = dec*9
    res = []
    while n:
        if n >= cur:
            n -= cur
            res.append(cur)
        if cur-dec <= 0:
            dec //= 10
            cur = dec*10
        cur -= dec
    print(len(res))
    print(*res)