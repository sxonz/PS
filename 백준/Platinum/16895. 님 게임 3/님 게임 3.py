n = int(input())
d = list(map(int,input().split()))
res = d[0]
cnt = 0
for i in d[1:]:
    res ^= i
if res == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i == j:
                continue
            tmp ^= d[j]
        if tmp <= d[i]:
            cnt += 1
    print(cnt)