testcase = int(input())
ans = []
for test in range(testcase):
    n = int(input())
    d = list(map(int,input().split()))
    inc = [d[0]]
    def lowbound(l,r,x):
        while l<r:
            mid = (l+r)//2
            if inc[mid] <= x:
                l = mid+1
            else:
                r = mid
        return r
    size = 1
    for i in d[1:]:
        if i > inc[-1]:
            inc.append(i)
            size += 1
        else:
            tmp = lowbound(0,size-1,i)
            if i < inc[tmp]:
                inc[tmp] = i
    ans.append(n-size)
for i in range(testcase):
    print(f'Case #{i+1}: {ans[i]}')
