for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))[::-1]
    maxv = 0
    ans = 0
    for i in d:
        if i < maxv:
            ans += maxv-i
        else:
            maxv = i
    print(ans)

