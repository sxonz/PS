n = int(input())
d = list(map(int,input().split()))
f = 0
if sum(d) == n:
    f = n%2
else:
    r = 0
    for i in d:
        r ^= i
    f = min(1,r)^1
print("kcouobsealgoav e r"[f::2])