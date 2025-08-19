import sys
sys.setrecursionlimit(300000)

N, K = map(int, input().split())

d = [[] for i in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    d[u].append((v, w))
    d[v].append((u, w))

vis = [False] * N
sub_sz = [0] * N
min_depth = [float('inf')] * (K + 1)
cur_tree = []

def get_size(cur, par):
    sub_sz[cur] = 1
    for v, w in d[cur]:
        if v == par or vis[v]:
            continue
        sub_sz[cur] += get_size(v, cur)
    return sub_sz[cur]

def get_cent(cur, par, thr):
    for v,w in d[cur]:
        if v == par or vis[v]:
            continue
        if sub_sz[v] > thr:
            return get_cent(v, cur, thr)
    return cur

def solve_path(cur, par, dist, depth):
    if dist > K:
        return float('inf')
    ret = min_depth[K - dist] + depth
    for v, w in d[cur]:
        if v == par or vis[v]:
            continue
        ret = min(ret, solve_path(v, cur, dist + w, depth + 1))
    return ret

def update(cur, par, dist, depth):
    if dist > K:
        return
    min_depth[dist] = min(min_depth[dist], depth)
    cur_tree.append(dist)
    for v, w in d[cur]:
        if v == par or vis[v]:
            continue
        update(v, cur, dist + w, depth + 1)

def dnc(cur):
    thr = get_size(cur, -1)
    ct = get_cent(cur, -1, thr // 2)
    vis[ct] = True
    
    ret = float('inf')
    for c in cur_tree:
        min_depth[c] = float('inf')
    cur_tree.clear()
    min_depth[0] = 0
    
    for v, w in d[ct]:
        if not vis[v]:
            ret = min(ret, solve_path(v, ct, w, 1))
            update(v, ct, w, 1)
    
    for v, w in d[ct]:
        if not vis[v]:
            ret = min(ret, dnc(v))
    
    return ret

ans = dnc(0)
print(-1 if ans == float('inf') else ans)
