testcase = int(input())
for t in range(testcase):
    n,*d = map(int,input().split())
    cur = -1
    cnt = 0
    for i in d:
        if not cnt:
            cnt = 1
            cur = i
        elif i == cur:
            cnt += 1
        else:
            cnt -= 1
    if d.count(cur) > n//2:
        print(cur)
    else:
        print("SYJKGW")