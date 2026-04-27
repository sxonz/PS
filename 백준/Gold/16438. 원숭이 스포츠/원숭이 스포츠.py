n = int(input())

d = [['A']*(n-1)+['B'] for _ in range(7)]

def dfs(s,e,depth):
    if depth == 7:
        return
    mid = (s+e) // 2
    for i in range(s,mid):
        d[depth][i] = 'A'
    for i in range(mid+1,e+1):
        d[depth][i] = 'B'
    dfs(s,mid,depth + 1)
    dfs(mid+1,e,depth+1)

dfs(0,n-1,0)
for i in d:
    print(''.join(i))