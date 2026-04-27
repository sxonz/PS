l,r,a = map(int,input().split())
while l<r and a:
    l += 1
    a -= 1
while r<l and a:
    r += 1
    a -= 1
print(min(r,l)*2+a//2*2)