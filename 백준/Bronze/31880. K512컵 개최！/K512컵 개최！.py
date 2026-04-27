n,m = map(int,input().split())
d = list(map(int,input().split()))
d2 = list(map(int,input().split()))
res = sum(d)
for i in d2:
    if i == 0:
        continue
    res *= i

print(res)