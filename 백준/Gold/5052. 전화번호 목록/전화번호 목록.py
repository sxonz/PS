testcase = int(input())
ans = []
for test in range(testcase):
    n = int(input())
    d = []
    for i in range(n):
        r = input()
        d.append((r+'0'*(10-len(r)),r,len(r)))
    d.sort()
    for i in range(1,n):
        if d[i-1][2] > d[i][2]:
            continue
        if d[i][1][:d[i-1][2]] == d[i-1][1]:
            ans.append("NO")
            break
    else:
        ans.append("YES")
for i in ans:
    print(i)