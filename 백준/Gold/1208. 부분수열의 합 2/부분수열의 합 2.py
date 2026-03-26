n,s = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
a = [0]
for i in range(n//2):
    tmp = []
    for j in a:
        tmp.append(j+d[i])
    for j in tmp:
        a.append(j)

b = [0]
for i in range(n//2,n):
    tmp = []
    for j in b:
        tmp.append(j+d[i])
    for j in tmp:
        b.append(j)

a.sort()
num = []
cnt = []
for i in a:
    if not num or num[-1] != i:
        num.append(i)
        cnt.append(0)
    cnt[-1] += 1

b = [s-i for i in b]
b.sort()
l = len(num)
idx = 0
ans = 0
for i in b:
    while idx<l and num[idx] < i:
        idx += 1
    k = 0
    if idx<l and num[idx] == i:
        ans += cnt[idx]
if s == 0:
    ans -= 1
print(ans)
