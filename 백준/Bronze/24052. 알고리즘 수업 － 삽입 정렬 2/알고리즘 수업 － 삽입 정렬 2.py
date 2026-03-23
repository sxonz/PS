n,k = map(int,input().split())
d = list(map(int,input().split()))
for i in range(1,n):
    loc = i-1
    new = d[i]

    while 0 <= loc and new < d[loc]:
        d[loc+1] = d[loc]
        k -= 1
        loc -= 1
        if not k:
            print(*d)
            exit()
    if loc+1 != i:
        d[loc+1] = new
        k -= 1
        if not k:
            print(*d)
            exit()
print(-1)