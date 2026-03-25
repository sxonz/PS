for t in range(int(input())):
    n = int(input())
    s,r = 0,0
    for i in range(n):
        a,b = map(float,input().split())
        s += a
        r += b*a
    print(int(s),r/s)