#와칠만세
n = int(input())
d = list(map(int,input().split()))

cnt = dict()
for i in d:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
v = tuple(cnt.values())

ans = 1
MOD = int(1e9)+7
for i in v:
    ans = ans * (i+1) % MOD
print(ans-1)