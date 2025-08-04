Y = "권병장님, 중대장님이 찾으십니다"
N = "엄마 나 전역 늦어질 것 같아"
n = int(input())
if n > 1:
    *a,end = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = [(i,j) for i,j in zip(a,b)]
    d.sort()
    last = d[0][0]+d[0][1]
    for i in range(1,n-1):
        if d[i][0] > last:
            print(N)
            break
        last = max(last,d[i][0]+d[i][1])
    else:
        if last >= end:
            print(Y)
        else:
            print(N)
else:
    print(Y)
