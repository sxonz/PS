n = int(input())
d = list(map(int,input().split()))
res = 0
for i in d:
    if i % 4 == 0:
        res ^= i-1
    elif i % 4 == 3:
        res ^= i+1
    else:
        res ^= i
if res == 0:
    print('cubelover')
else:
    print('koosaga')