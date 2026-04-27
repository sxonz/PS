for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    d.sort()
    ans = max(d[1]-d[0],d[-1]-d[-2])
    for i in range(n-2):
        ans = max(ans,d[i+2]-d[i])
    print(ans)