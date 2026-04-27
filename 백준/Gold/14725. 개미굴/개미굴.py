n = int(input())
d = dict()
for i in range(n):
    n,*r = input().split()
    cur = d
    for i in r:
        if i not in cur:
            cur[i] = {}
        cur = cur[i]
def dfs(cur,depth,name):
    if depth+1:
        print("--"*depth + name)
    for i in sorted(cur.keys()):
        dfs(cur[i],depth+1,i)
dfs(d,-1,'Root')
