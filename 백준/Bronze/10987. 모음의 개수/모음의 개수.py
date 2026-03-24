s = input()
ans = 0
for i in "aeiou":
    ans += s.count(i)
print(ans)