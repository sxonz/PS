for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if d[j] > d[j+1]:
                d[j],d[j+1] = d[j+1],d[j]
                ans += 1
    print(ans)
