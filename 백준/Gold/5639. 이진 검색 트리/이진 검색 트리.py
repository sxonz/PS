import sys
sys.setrecursionlimit(20000)
d = []
try:
    while True:
        d.append(int(input()))
except:
    pass

def dfs(l, r):
    if l > r:
        return
    mid = r + 1
    for i in range(l+1, r+1):
        if d[i] > d[l]:
            mid = i
            break
    dfs(l+1, mid-1)
    dfs(mid, r)
    print(d[l])

dfs(0, len(d)-1)