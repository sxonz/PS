d = dict()
for i in range(10):
    d[str(i)] = i

for i in range(65,91):
    d[chr(i)] = i-55

s,n = input().split()
n = int(n)
val = []
for i in s:
    val.append(d[i])

ans = 0
for v,i in zip(range(len(s)-1,-1,-1),val):
    ans += i*n**v
print(ans)