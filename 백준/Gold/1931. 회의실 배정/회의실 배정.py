n = int(input())
d = []
for _ in range(n):
    s,e = map(int,input().split())
    d.append((e,s))
d.sort()
cur = 0
cnt = 0
for e,s in d:
    if s >= cur:
        cur = e
        cnt += 1
print(cnt)