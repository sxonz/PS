n,k = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
for i in d:
    if k >= i:
        k += 1
print(k)