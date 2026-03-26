
n = int(input())
d = list(map(int,input().split()))

a1 = []
a2 = [0]*400001
pivot = 200000
ans = 0
for i in range(n):
    for k in range(i):
        if a2[d[i]-d[k]+pivot]:
            ans += 1
            break
    a1.append(d[i])
    for j in a1:
        a2[j+d[i]+pivot] = 1
print(ans)
