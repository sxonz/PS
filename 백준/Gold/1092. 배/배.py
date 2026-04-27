n = int(input())
crain = list(map(int,input().split()))
crain.sort()
m = int(input())
box = list(map(int,input().split()))
box.sort()

x = 0
while m:
    x += 1
    cidx = n-1
    bidx = m-1
    flag = True
    while cidx >= 0 and bidx >= 0:
        if crain[cidx] >= box[bidx]:
            cidx -= 1
            box.pop(bidx)
            m -= 1
            flag = False
        bidx -= 1
    if flag:
        print(-1)
        break
else:
    print(x)