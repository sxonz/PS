import sys
input = sys.stdin.readline

n = int(input())
r = range(n)
d = [list(map(int,input().split())) for i in range(n)]
ab = []
for i in r:
    for j in r:
        ab.append(d[i][0]+d[j][1])
ab.sort()

num = []
cnt = []
for i in ab:
    if not num or num[-1] != i:
        num.append(i)
        cnt.append(1)
    else:
        cnt[-1] += 1
l = len(num)

cd = []
for i in r:
    for j in r:
        cd.append(-d[i][2]-d[j][3])
cd.sort()

ans = 0
idx = 0
for i in cd:
    while idx < l and num[idx] < i:
        idx += 1
    if idx<l and num[idx] == i:
        ans += cnt[idx]
print(ans)