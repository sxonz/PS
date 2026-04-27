n,m,t = map(int,input().split())
d = list(map(int,input().split()))
cur = [0]*m

for i in d:
    idx = 0
    tmp = cur[0]
    for j in range(1,m):
        if cur[j] < tmp:
            tmp = cur[j]
            idx = j
    cur[idx] += i
if min(cur) > t:
    print("GO")
else:
    print("WAIT")
    