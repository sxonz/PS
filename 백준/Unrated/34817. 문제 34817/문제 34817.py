n,k = map(int,input().split())
d = list(map(int,input().split()))
maxv = 0
flag = False
for i in d:
    maxv = max(maxv,i)
    if maxv > i and maxv-i > k:
        flag = True
        break
print("YNEOS"[flag::2])
