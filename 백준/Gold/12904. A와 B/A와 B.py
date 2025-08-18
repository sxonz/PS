s = input()
e = input()
for i in range(len(e)-len(s)):
    if e[-1] == "A":
        e = e[:-1]
    else:
        e = e[:-1][::-1]
print((s == e)%2)