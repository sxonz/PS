def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p2[1]) - (p3[0]-p2[0])*(p2[1]-p1[1])


n,px,py =  map(int,input().split())
d = [(px,py)]+[tuple(map(int,input().split())) for i in range(n)]

cur = 0
while len(d) >= 2:
    d.sort()

    hull = [[],[]]
    for i in range(2):
        stack = [0,1]
        for p in range(2,len(d)):
            while len(stack) >= 2 and ccw(d[stack[-2]],d[stack[-1]],d[p]) < 0:
                stack.pop()
            stack.append(p)
        hull[i] = stack[1:]
        d.reverse()

    hull[1] = [len(d)-1-i for i in hull[1]]
    s = hull[0]+hull[1]

    idx = d.index((px,py))
    s.sort(reverse=True)
    for i in s:
        if i == idx:
            print(cur)
            exit(0)
        d.pop(i)
    cur += 1
print(cur)