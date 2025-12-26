a,b = map(int,input().split())
l,r = 0,0
while a >= 1 and b >= 1:
    if b>a:
        r += b//a
        b %= a
    else:
        l += a//b
        a %= b
if not a:
    l -= 1
if not b:
    r -= 1
print(l,r)
