n = int(input())
d = list(map(int,input().split()))
res = d[0]
for i in d[1:]:
    res ^= i
if res != 0:
    print('koosaga')
else:
    print('cubelover')