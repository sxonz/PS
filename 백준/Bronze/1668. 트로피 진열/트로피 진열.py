n = int(input())
d = [int(input()) for i in range(n)]
maxv = 0
l,r = 0,0
for i in d:
    if i>maxv:
        l += 1
        maxv = i
maxv = 0
for i in d[::-1]:
    if i>maxv:
        r += 1
        maxv = i
print(l)
print(r)