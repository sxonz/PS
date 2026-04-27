s,one,zero = map(int,input().split())
u = 0
for _ in range(one+zero):
    r = int(input())
    if r == 1:
        u += 1
        if u > s:
            s *= 2
    else:
        u -= 1
print(s)
