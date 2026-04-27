for t in range(int(input())):
    k,n = map(int,input().split())
    d = [tuple(map(int,input().split())) for i in range(n)]
    d = [i*j for i,j in d]
    d.sort(reverse=True)
    for i in range(n):
        k -= d[i]
        if k <= 0:
            print(i+1)
            break