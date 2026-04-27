s = input().split('-')
d = []
for i in s:
    d.append(sum(list(map(int,i.split('+')))))
ans = 0
if d:
    ans += d.pop(0)
for i in d:
    ans -= i
print(ans)