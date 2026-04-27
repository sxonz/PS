from collections import deque
fib = [1,1]
while fib[-1] < 1000000001:
    fib.append(fib[-1]+fib[-2])
l = len(fib)

res = [deque([])]
for test in range(int(input())):
    n = int(input())

    while n:
        for i in reversed(range(l)):
            if n >= fib[i]:
                res[-1].appendleft(str(fib[i]))
                n -= fib[i]
    res.append(deque([]))
res.pop()
for i in res:
    print(' '.join(i))