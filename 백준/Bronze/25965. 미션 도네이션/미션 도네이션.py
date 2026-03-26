for t in range(int(input())):
    n = int(input())
    d = [tuple(map(int,input().split())) for i in range(n)]
    kda = list(map(int,input().split()))
    ans = 0
    for i in d:
        ans += max(0,i[0]*kda[0]-i[1]*kda[1]+i[2]*kda[2])
    print(ans)