n = int(input())
d = [int(input()) for i in range(n)]
print(round(sum(d)/n))
d.sort()
print(d[n//2])
cnt = dict()
for i in d:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
r = sorted(list(set(d)),key=lambda x:(-cnt[x],x))
if n != 1 and cnt[r[0]] == cnt[r[1]]:
    r.pop(0)
print(r[0])
print(max(d)-min(d))