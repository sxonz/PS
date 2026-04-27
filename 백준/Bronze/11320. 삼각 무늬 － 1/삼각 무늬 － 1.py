for t in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    cur = 1
    for i in range(a//b):
        ans += cur
        cur += 2
    print(ans)