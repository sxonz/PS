s = input()
n = len(s)
i = 0
ans = ''
while i<n:
    if s[i:i+4] == "XXXX":
        ans += "AAAA"
        i += 4
    elif s[i:i+2] == "XX":
        ans += "BB"
        i += 2
    else:
        ans += s[i]
        i += 1
if "X" not in ans:
    print(ans)
else:
    print(-1)
