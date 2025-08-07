m,n = map(int, input().split())
prime = [0]+[1]*n

for i in range(2, n+1):
    if prime[i] and m <= i:
        print(i)
    for j in range(i * 2, n+1, i):
        prime[j] = 0
