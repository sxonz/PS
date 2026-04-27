s = input()
res = 1
if not s:
    res = 0
else:
    res = {'c':26,'d':10}[s[0]]
for i in range(1,len(s)):
    if s[i] == 'c':
        if s[i-1] == 'c':
            res *= 25
        else:
            res *= 26
    else:
        if s[i-1] == 'd':
            res *= 9
        else:
            res *= 10
    res %= 1000000009
print(res)