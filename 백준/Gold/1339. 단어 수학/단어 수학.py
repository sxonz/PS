n = int(input())
d = [input()[::-1] for _ in range(n)]
tmp = ''.join(d)
count = dict()

for i in tmp:
    count[i] = 0

for i in d:
    l = len(i)
    for j in range(l):
        count[i[j]] += 10**(j)
k = 9
ans = 0
for i in sorted([count[j] for j in count],reverse=True):
    ans += k*i
    k -= 1
print(ans)