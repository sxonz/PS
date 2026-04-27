s = input()
n = len(s)
d = set()
for i in range(n+1):
    for j in range(i+1,n+1):
        d.add(s[i:j])
print(len(d))