while True:
    s = input()
    if s == "0":
        break
    n,p = map(int,s.split())
    d = [[] for i in range(n)]
    for i in range(0,n//2,2):
        d[i] = [i+2,n-i-1,n-i]
        d[i+1] = [i+1,n-i-1,n-i]
        d[n-i-2] = [i+1,i+2,n-i]
        d[n-i-1] = [i+1,i+2,n-i-1]
    print(*d[p-1])