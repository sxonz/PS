def ccw(p1,p2,p3):
    return (p2[0]-p1[0]) * (p3[1]-p2[1]) - (p2[1]-p1[1]) * (p3[0]-p2[0])
testcase = int(input())
for test in range(testcase):
    n = int(input())
    d = []
    for i in range(n//5+(1 if (n%5) else 0)):
        d += list(map(int,input().split()))
    d = [(d[i*2],d[i*2+1]) for i in range(n)]
    d.sort()
    ans = []
    for j in range(2):
        hull = [d[0],d[1]]
        for i in d[2:]:
            while len(hull) >= 2 and ccw(hull[-2],hull[-1],i) >= 0:
                hull.pop()
            hull.append(i)
        
        ans += hull[:-1]
        d = d[::-1]
    print(len(ans))
    first = ans.index(min(ans,key=lambda x:(-x[1],x[0])))
    for i in ans[first:]:
        print(*i)
    for i in ans[:first]:
        print(*i)