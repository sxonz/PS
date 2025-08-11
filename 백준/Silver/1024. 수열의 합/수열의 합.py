n,k = map(int, input().split())

for i in range(k, 101):
    x = n/i - (i+1)/2
    if x == int(x):
        x = int(x)
        if x >= -1:
            print(*range(x+1, x+i+1))
            break
else:
    print(-1)