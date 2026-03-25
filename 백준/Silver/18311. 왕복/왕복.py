n,k = map(int,input().split())
d = list(map(int,input().split()))
for i in range(n):
    k -= d[i]
    if k < 0:
        print(i+1)
        break
else:
    for i in range(n-1,-1,-1):
        k -= d[i]
        if k<0:
            print(i+1)
            break