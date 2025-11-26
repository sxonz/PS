from collections import deque
input = iter(open(0).read().split('\n')).__next__

m,n,o,p,q,r,s,t,u,v,w = map(int,input().split())
visited = [[[[[[[[[[[0]*m for ni in range(n)] for oi in range(o)] for pi in range(p)] for qi in range(q)] for ri in range(r)] for si in range(s)] for ti in range(t)] for ui in range(u)] for vi in range(v)] for wi in range(w)]
tomato = deque([])
d = []
cnt = 0
for wi in range(w):
    wd = []
    for vi in range(v):
        vd = []
        for ui in range(u):
            ud = []
            for ti in range(t):
                td = []
                for si in range(s):
                    sd = []
                    for ri in range(r):
                        rd = []
                        for qi in range(q):
                            qd = []
                            for pi in range(p):
                                pd = []
                                for oi in range(o):
                                    od = []
                                    for ni in range(n):
                                        tmp = list(map(int,input().split()))
                                        for i in range(m):
                                            if tmp[i] == 1:
                                                tomato.append((wi,vi,ui,ti,si,ri,qi,pi,oi,ni,i,0))
                                            elif tmp[i] == 0:
                                                cnt += 1
                                        od += [tmp]
                                    pd += [od]
                                qd += [pd]
                            rd += [qd]
                        sd += [rd]
                    td += [sd]
                ud += [td]
            vd += [ud]
        wd += [vd]
    d += [wd]

dw = [ 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
dv = [ 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
du = [ 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
dt = [ 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
ds = [ 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
dr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
dq = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0 ]
dp = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0, 0, 0 ]
do = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0, 0, 0 ]
dn = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1, 0, 0 ]
dm = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1 ]

mday = 0
while tomato and cnt:
    cw,cv,cu,ct,cs,cr,cq,cp,co,cn,cm,day = tomato.popleft()
    if day + 1 > mday:
        mday = day + 1

    for i in range(22):
        nw = cw + dw[i]
        nv = cv + dv[i]
        nu = cu + du[i]
        nt = ct + dt[i]
        ns = cs + ds[i]
        nr = cr + dr[i]
        nq = cq + dq[i]
        np = cp + dp[i]
        no = co + do[i]
        nn = cn + dn[i]
        nm = cm + dm[i]

        if not (0 <= nw < w and 0 <= nv < v and 0 <= nu < u and 0 <= nt < t and 0 <= ns < s and 0 <= nr < r and 0 <= nq < q and 0 <= np < p and 0 <= no < o and 0 <= nn < n and 0 <= nm < m):
            continue

        if d[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0 and visited[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
            visited[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
            d[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
            cnt -= 1
            tomato.append((nw,nv,nu,nt,ns,nr,nq,np,no,nn,nm,day+1))
if cnt:
    print(-1)
else:
    print(mday)