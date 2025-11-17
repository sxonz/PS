t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
s1 = dict()
s2 = dict()
p1 = [0,a[0]]
p2 = [0,b[0]]

for i in a[1:]:
    p1 += [p1[-1]+i]

for i in b[1:]:
    p2 += [p2[-1]+i]

for i in range(1,n+1):
    for j in range(i):
        tmp = p1[i] - p1[j]
        if tmp not in s1:
            s1[tmp] = 1
        else:
            s1[tmp] += 1

for i in range(1,m+1):
    for j in range(i):
        tmp = p2[i] - p2[j]
        if tmp not in s2:
            s2[tmp] = 1
        else:
            s2[tmp] += 1

ans = 0
for i in s1:
    if t-i in s2:
        ans += s1[i]*s2[t-i]
print(ans)