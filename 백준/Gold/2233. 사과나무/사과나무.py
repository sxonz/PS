n = int(input())
bug = input()[1:]
parents = [0]*(n+1)
depth = [0]*(n+1)
d = {0:1}
idx = 0
def dfs(x):
    global idx
    cnt = 0
    while bug[idx] == '0':
        cnt += 1
        idx += 1
        d[idx] = x+cnt
        parents[x+cnt] = x
        depth[x+cnt] = depth[x] + 1
        cnt += dfs(x+cnt)
    idx += 1
    d[idx] = x
    return cnt
dfs(1)
a,b = map(int,input().split())
a,b = d[a-1],d[b-1]
if depth[a]>depth[b]:a,b = b,a
while depth[b] > depth[a]:
    b = parents[b]
while a != b:
    a,b = parents[a],parents[b]
print(*[i+1 for i in d if d[i] == a])