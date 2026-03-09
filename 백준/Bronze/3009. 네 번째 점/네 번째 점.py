a = []
b = []
for i in range(3):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()
print(sum(a)-a[1]*2,sum(b)-b[1]*2)