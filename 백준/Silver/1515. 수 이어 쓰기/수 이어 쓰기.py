s = list(input())
n = 0
while s:
    n += 1
    for i in str(n):
        if not s:
            break
        if i == s[0]:
            s.pop(0)
print(n)