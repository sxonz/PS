n,m = map(int,input().split())
d = []
for i in range(n):
    d += list(map(int,input().split()))

cnt = dict()
for i in d:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1

flag = 0
if m%2:
    tmp = sum(i%2 for i in cnt.values())
    flag = (n - tmp)%2^1 and tmp <= n
else:
    flag = all(i%2^1 for i in cnt.values())
print("YNEOS"[flag^1::2])