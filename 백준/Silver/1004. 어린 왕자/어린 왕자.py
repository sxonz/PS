testcase = int(input())
for test in range(testcase):
    cnt = 0   
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for i in range(n):
        cx,cy,r = map(int,input().split())
        dist1 = (x1-cx)**2 + (y1-cy)**2
        dist2 = (x2-cx)**2 + (y2-cy)**2
        if dist1<(s:=r**2) and dist2<s:
            continue
        if s > dist1 or s > dist2:
            cnt +=1

    print(cnt)