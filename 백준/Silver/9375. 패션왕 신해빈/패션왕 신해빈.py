testcase = int(input())
 
for test in range(testcase):
    n = int(input())
    d = {}
    for i in range(n):
        c,k = map(str, input().split())
        if k not in d:
            d[k] = 0
        d[k] += 1
    ans = 1
    for v in d.values():
        ans *= v + 1
    print(ans-1)