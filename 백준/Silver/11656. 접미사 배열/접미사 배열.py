s = input()
n = len(s)
d = []
for i in range(n):
    d.append(s[i:])
d.sort()
print(*d,sep='\n')