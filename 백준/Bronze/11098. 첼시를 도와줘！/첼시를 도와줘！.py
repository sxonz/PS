for t in range(int(input())):
    n = int(input())
    maxv = 0
    ans = ''
    for i in range(n):
        a,b = input().split()
        if int(a) > maxv:
            maxv = int(a)
            ans = b
    print(ans)