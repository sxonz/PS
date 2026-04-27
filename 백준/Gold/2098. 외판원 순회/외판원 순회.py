M = (10 ** 25)

N = int(input())
d = [list(map(int,input().split())) for _ in range(N)]

dp = {}

def DFS(x, visited):
    if visited == (1 << N) - 1:
        if d[x][0]:
            return d[x][0]
        else:
            return M

    if (x, visited) in dp:
        return dp[(x, visited)]

    min_cost = M
    for nx in range(1, N):

        if d[x][nx] == 0 or visited & (1 << nx):
            continue

        cost = DFS(nx, visited | (1 << nx)) + d[x][nx]
        min_cost = min(cost,min_cost)

    dp[(x, visited)] = min_cost 
    return min_cost


tmp = DFS(0, 1)
if tmp > 10 ** 20:
    print(-1)
else:
    print(tmp)