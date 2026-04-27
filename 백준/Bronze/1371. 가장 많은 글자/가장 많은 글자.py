s = ''
try:
    while True:
        s += input()
except:
    pass
s = s.replace(" ","")
cnt = dict()
for i in s:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
ans = ''
m = max(cnt.values())
for i in cnt:
    if cnt[i] == m:
        ans += i
ans = sorted(list(ans))
print(''.join(ans))