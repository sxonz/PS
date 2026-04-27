for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    vis = dict()
    idx = 0
    ans = []
    for i in range(n):
        while d[idx] in vis and vis[d[idx]]:
            vis[d[idx]] -= 1
            idx += 1
        ans.append(d[idx])
        if d[idx]*4//3 not in vis:
            vis[d[idx]*4//3] = 0
        vis[d[idx]*4//3] += 1
        idx += 1
    print(f"Case #{t+1}: ",end='')
    print(*ans)
        
        