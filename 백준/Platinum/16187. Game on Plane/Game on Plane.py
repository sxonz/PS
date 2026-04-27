d = [0]*5001
d[2] = 1
for i in range(3,5001):
    mex = [0 for _ in range(5001)]
    l = 0
    r = i-2
    while r >= l:
        mex[d[l]^d[r]] = 1
        l += 1
        r -= 1
    for j in range(1000):
        if mex[j] == 0:
            d[i] = j
            break

for i in range(int(input())):
    temp = d[int(input())]

    temp = 'First' if temp else 'Second'
    print(temp)