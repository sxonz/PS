n,ans,cnt= int(input()),[],dict()
for i in range(n):
    c = input()[0]
    if c not in cnt:cnt[c] = 0
    cnt[c] += 1
    if cnt[c] == 5:ans.append(c)
if ans:print(''.join(sorted(ans)))
else:print("PREDAJA")