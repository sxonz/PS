s = input()
ans = 0
for i in range(26):
    for j in range(i+1, 26):
        a, b = chr(65+i), chr(65+j)
        a1, a2 = s.find(a), s.rfind(a)
        b1, b2 = s.find(b), s.rfind(b)
        if a1<b1<a2<b2 or b1<a1<b2<a2:
            ans += 1
print(ans)