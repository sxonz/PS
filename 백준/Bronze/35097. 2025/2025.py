while True:
    n = int(input())
    if not n:
        break
    tmp = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            tmp += i*j
    print(tmp)