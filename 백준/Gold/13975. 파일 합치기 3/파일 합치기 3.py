from heapq import *
testcase = int(input())
res = []
for _ in range(testcase):
    n = int(input())
    d = list(map(int,input().split()))
    heapify(d)
    ans = 0
    while len(d) > 1:
        a,b = heappop(d),heappop(d)
        ans += a+b
        heappush(d,a+b)
    res.append(ans)
for i in res:
    print(i)