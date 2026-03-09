d = dict()
for i in range(10):
    d[i] = str(i)

for i in range(65,91):
    d[i-55] = chr(i)

r,n = map(int,input().split())
ans = ""
while r:
    ans += d[r%n]
    r //= n
print(ans[::-1])

