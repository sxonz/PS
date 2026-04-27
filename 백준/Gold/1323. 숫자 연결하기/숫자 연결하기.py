n,k = map(int, input().split())
cur = n%k
i = 1
loop = set()
while cur != 0:
    if cur in loop:
        print(-1)
        break
    loop.add(cur)
    cur = (cur * (10 ** len(str(n))) + n) % k
    i += 1
else:
    print(i)
