w,h = map(int, input().split())
p,q = map(int, input().split())
t = int(input())

a = (p + t) // w
b = (q + t) // h

if a%2:
    x = w - (p+t)%w
else: 
    x = (p+t)%w
if b%2:
    y = h - (q+t)%h
else:
    y = (q+t)%h
print(x, y)