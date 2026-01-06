n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
def solve(cur,idx):
    if idx == n:
        return sum([1 for i in cur if i[0] <= 0])
    if cur[idx][0] <= 0:
        return solve(cur,idx+1)

    m = 0
    flag = True
    tmp = [j[::] for j in cur]
    for i in range(n):
        if cur[i][0] <= 0 or idx == i:
            continue
        flag = False
        t1,t2 = tmp[idx][::],tmp[i][::]
        tmp[idx],tmp[i] = [tmp[idx][0]-tmp[i][1],tmp[idx][1]], [tmp[i][0]-tmp[idx][1],tmp[i][1]]
        m = max(m,solve(tmp,idx+1))
        tmp[idx],tmp[i] = t1,t2
    
    return n-1 if flag else m

print(solve(d,0))