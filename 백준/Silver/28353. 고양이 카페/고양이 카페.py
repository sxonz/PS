n,k = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
cnt = 0
while True:
    flag = False

    idx = 0
    for i in range(len(d)-1,0,-1):
        if d[i] + d[0] <= k:
            cnt += 1
            idx = i
            flag = True
            break

    if not flag or len(d) < 2:
        break

    d.pop(idx)
    d.pop(0)
print(cnt)
