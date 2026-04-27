def check(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

r, m = 0, None
start,end=int(input()),int(input())
for i in range(start, end + 1):
    if check(i):
        if m is None:
            m = i
        r += i

if r == 0:
    print(-1)
else:
    print(r)
    print(m)

    