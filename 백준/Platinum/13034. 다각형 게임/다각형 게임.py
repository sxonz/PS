d = [0]*1001
d[2] = 1
for i in range(3,1001):
    mex = [0 for _ in range(1001)]
    l = 0
    r = i-2
    while r >= l:
        mex[d[l]^d[r]] = 1
        l += 1
        r -= 1
    for j in range(1001):
        if mex[j] == 0:
            d[i] = j
            break

temp = d[int(input())]

temp = 1 if temp else 2
print(temp)