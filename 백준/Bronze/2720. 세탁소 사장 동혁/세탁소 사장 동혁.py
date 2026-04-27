coin=[25,10,5,1]
for i in range(int(input())):
    n = int(input())
    d = [0,0,0,0]
    for j in range(4):
        while coin[j] <= n:
            d[j] += 1
            n -= coin[j]
    print(*d)