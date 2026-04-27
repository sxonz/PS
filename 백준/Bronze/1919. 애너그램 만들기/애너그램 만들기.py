a = input()
b = input()
cnt = dict()
for i in a:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
for i in b:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] -= 1
print(sum([abs(i) for i in cnt.values()]))