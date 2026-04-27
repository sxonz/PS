n,m = map(int,input().split())
res = 0
for t in range(n):
    d = list(map(int,input().split()))
    res ^= sum(d)
if res == 0:
    print('ainta')
else:
    print('august14')