N = 250000
arr = [False]*2 + [True]*(N-1)
i = 2

for i in range(2,N+1):
    if arr[i]:
        for j in range(i + i, N + 1, i):
            if arr[j]:
                arr[j] = False

while True:
    n = int(input())
    if  not n:
        break
    print(sum(arr[n+1:2*n+1]))