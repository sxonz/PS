t = int(input())

for t in range(t):
    a,b,c = map(int, input().split())
    if b == 1:
        result = pow(a, a, c)
    else:
        x = pow(a, a)
        result = pow(x, x, c)
    print(f"Case #{t+1}: {result}")
