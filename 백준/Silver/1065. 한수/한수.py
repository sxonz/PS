n = int(input())
ans = 0
for i in range(1,n+1):
    i = str(i)
    a = set()
    for j in range(len(i)-1):
        a.add(int(i[j+1])-int(i[j]))
    if len(a) <= 1:
        ans += 1
print(ans)