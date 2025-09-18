n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
cur = -int(1e12)
cnt = 0
d.sort()

for start, end in d:
    r = end - max(start,cur)
    if r > 0:
        cnt += r
    cur = max(cur,end)
print(cnt)