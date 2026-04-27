testcase = int(input())
ans = []
for i in range(testcase):
    s = input().split(",")
    d = []
    for j in s:
        d += [j.split(":")]
    r = dict()
    for a,b in d:
        r[a] = int(b)
    s = input().split("|")
    d = []
    for j in s:
        d += [j.split("&")]
    m = int(1e6)
    for j in d:
        tmp = 0
        for k in j:
            tmp = max(tmp,r[k])
        m = min(tmp,m)
    ans.append(m)
for i in ans:
    print(i)