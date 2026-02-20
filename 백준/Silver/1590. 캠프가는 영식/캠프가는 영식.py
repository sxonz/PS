n,t = map(int,input().split())
d = []
for i in range(n):
    a,b,c = map(int,input().split())
    for i in range(c):
        d.append(a+b*i)
d.sort()
if d[-1] < t:
    print(-1)
else:
    for i in d:
        if i >= t:
            print(i-t)
            break