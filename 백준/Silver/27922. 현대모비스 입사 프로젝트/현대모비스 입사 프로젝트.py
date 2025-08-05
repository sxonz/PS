n,k = map(int,input().split())
a,b,c = [],[],[]
for i in range(n):
    x,y,z = map(int,input().split())
    a.append(x+y)
    b.append(y+z)
    c.append(x+z)
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
print(max(sum(a[:k]), sum(b[:k]), sum(c[:k])))