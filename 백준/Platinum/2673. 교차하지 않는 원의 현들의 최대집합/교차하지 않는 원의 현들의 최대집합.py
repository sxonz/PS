n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
d = [tuple(sorted(i)) for i in d]
def direction(p1,p2):
    return 0 <= p2-p1 <= 50 or p2-p1 <= -50
def cross(s1,e1,s2,e2):
    if direction(s1,e1) == direction(s1,s2) and direction(e1,s1) == direction(e1,s2):
        return not (direction(s1,e1) == direction(s1,e2) and direction(e1,s1) == direction(e1,e2))
    if direction(s1,e1) == direction(s1,e2) and direction(e1,s1) == direction(e1,e2):
        return not(direction(s1,e1) == direction(s1,s2) and direction(e1,s1) == direction(e1,s2))
    return 0

graph = [set() for i in range(n)]
no = [set() for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if cross(*d[i],*d[j]):
            no[i].add(j)
        else:
            graph[i].add(j)

ans = 1
def back(idx,cur,l,exc):
    global ans,r
    ans = max(ans,l)

    if n-idx+l <= ans or idx >= n:
        return
    tmp = l
    for i in range(idx,n):
        if i not in exc:
            tmp += 1
    if tmp <= ans:
        return
    if idx not in exc:
        for i in cur:
            if i not in graph[idx]:
                break
        else:
            l += 1
            cur.add(idx)
            exc |= no[idx]
            back(idx+1,cur,l,exc)
            l -= 1
            cur.discard(idx)
            exc -= no[idx]
    back(idx+1,cur,l,exc)
back(0,set(),0,set())
print(ans)