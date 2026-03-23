n = int(input())
d = list(map(int,input().split()))
r = list(map(int,input().split()))
cur = d[0]
maxv,minv = -int(1e12),int(1e12)
def back(idx):
    global cur,maxv,minv
    if idx == n:
        maxv = max(maxv,cur)
        minv = min(minv,cur)
        return
    if r[0]:
        r[0] -= 1
        cur += d[idx]
        back(idx+1)
        r[0] += 1
        cur -= d[idx]
    if r[1]:
        r[1] -= 1
        cur -= d[idx]
        back(idx+1)
        r[1] += 1
        cur += d[idx]
    if r[2]:
        r[2] -= 1
        cur *= d[idx]
        back(idx+1) 
        r[2] += 1
        cur //= d[idx]
    if r[3]:
        r[3] -= 1
        tmp = cur
        if cur < 0:
            cur = -(-cur//d[idx])
        else:
            cur //= d[idx]
        back(idx+1)
        r[3] += 1
        cur = tmp
back(1)
print(maxv)
print(minv)