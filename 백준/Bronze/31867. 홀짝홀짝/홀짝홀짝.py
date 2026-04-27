n = int(input())
k = sum([int(i) % 2 for i in input()])
if k * 2 == n:
    print(-1)
elif k * 2 > n:
    print(1)
else:
    print(0)
