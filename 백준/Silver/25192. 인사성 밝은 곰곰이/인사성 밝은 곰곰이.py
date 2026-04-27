n = int(input())
d = dict()
used = []
ans = 0
for t in range(n):
    s = input()
    if s == "ENTER":
        for i in used:
            d[i] = 1
        used.clear()
    else:
        if s not in d:
            d[s] = 1
        if d[s]:
            d[s] = 0
            used.append(s)
            ans += 1
print(ans)