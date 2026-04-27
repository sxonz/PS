s = input()
n = len(s)
f = s[-1] in  "aeiouns"
for i,j in enumerate(reversed(s)):
    if j in "aeiou":
        if f:
            f = 0
            continue
        print(n-i)
        break
else:
    print((-1))