q = int(input())
d = [input().split() for i in range(q)][::-1]
ans = ''
l = int(1e10)
for q,s,t in d:
    t = int(t)
    if t >= l:
        continue
    if q == "type":
        ans += s
    else:
        l = t-int(s)

print(ans[::-1])