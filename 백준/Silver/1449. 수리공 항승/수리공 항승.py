n,l = map(int,input().split())
d = list(map(int,input().split()))
d.sort()
cnt = 0
last = 0
for i in d:
    if i <= last:
        continue
    cnt += 1
    last = i+l-1
print(cnt)