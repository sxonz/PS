a,b,c=map(int,input().split())
d = int(input())
c += d
e,f = divmod(c,60)
c = f
b += e
g,h = divmod(b,60)
b = h
a += g
a %= 24
print(a,b,c)