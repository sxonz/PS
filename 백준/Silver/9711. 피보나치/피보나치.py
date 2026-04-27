testcase = int(input())
ans = []
for test in range(testcase):
    p,q = map(int,input().split())
    bef = cur = 1
    for i in range(p-2):
        cur = (bef + (bef := cur%q))%q
    ans.append((test+1,cur%q))
for i,r in ans:
    print(f"Case #{i}: {r}")