n,k = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(n)]
d.sort()
maxa = [(0,0)]
maxb = [(0,0)]
for t,a,b in d:
    maxa.append((t,max(a,maxa[-1][1])))
    maxb.append((t,max(b,maxb[-1][1])))
l = len(maxb)
ans = max(i[1]+i[2] for i in d)
idx = 0
for i in range(n,-1,-1):
    while idx<l-1 and maxa[i][0]+maxb[idx+1][0] <= k:
        idx += 1
    ans = max(ans,maxa[i][1]+maxb[idx][1])
print(ans)