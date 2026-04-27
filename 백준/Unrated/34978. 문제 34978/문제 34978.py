n = int(input())
d = dict()
for i in range(n):
    c,n,*r = input().split()
    d[c] = []
    for j in r:
        d[c].append(j)
s = input()
for i in range(len(s)-1):
    if s[i] in d and s[i+1] not in d[s[i]]:
        print("no")
        break
else:
    print("yes")