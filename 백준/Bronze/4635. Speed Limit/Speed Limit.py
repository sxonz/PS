while True:
    n = int(input())
    if n == -1:break
    cur,res = 0,0
    for i in range(n):
        s,t = map(int,input().split())
        res += s * (t-cur)
        cur = t
    print(f"{res} miles")

