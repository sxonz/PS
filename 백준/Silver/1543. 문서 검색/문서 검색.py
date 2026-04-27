a = input()
b = input()
ans = 0
n = len(b)
while b in a:
    ans += 1
    a = a[a.index(b)+n:]
print(ans)