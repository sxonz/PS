n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
start = []
link = []
s,l = 0,0
ans = int(1e9)
def back(idx):
    global s,l,ans
    if len(start) > n//2 or len(link) > n//2:
        return
    if idx == n:
        ans = min(ans,abs(s-l))
        return
    
    tmp = 0
    for i in start:
        tmp += d[idx][i] + d[i][idx]
    s += tmp
    start.append(idx)
    back(idx+1)
    start.pop()
    s -= tmp

    tmp = 0
    for i in link:
        tmp += d[idx][i] + d[i][idx]
    l += tmp
    link.append(idx)
    back(idx+1)
    link.pop()
    l -= tmp
back(0)
print(ans)