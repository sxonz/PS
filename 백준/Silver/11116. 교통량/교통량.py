testcase = int(input())
ans = []
for _ in range(testcase):
    n = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    l.sort()
    cnt = 0
    for i in l:
        if i+500 in l and i+1000 in r and i+1500 in r:
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i)