n = int(input())
d = [0]*n
l,r = 0,n-1
for i in range(1,n+1):
    if i%2:
        d[l] = i
        l += 1
    else:
        d[r] = i
        r -= 1
print(*d)