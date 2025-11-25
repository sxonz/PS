n = int(input())
d = list(map(int,input().split()))
idx = list(range(n))
idx.sort(key=lambda x:d[x])

res = [0]*n
trie = [0,0,0]
def dfs(cur,rem):
    if not rem:
        cur[2] = 1
        return ''
    ans = ''
    if not cur[0]:
        cur[0] = [0,0,0]
        ans += '0' + dfs(cur[0],rem-1)
    elif not cur[1]:
        cur[1] = [0,0,0]
        ans += '1' + dfs(cur[1],rem-1)
    elif not cur[0][2]:
        ans += '0' + dfs(cur[0],rem-1)
    elif not cur[1][2]:
        ans += '1' + dfs(cur[1],rem-1)
    else:
        print(-1)
        exit()
    if cur[0] and cur[0][2] and cur[1] and cur[1][2]:
        cur[2] = 1
    return ans
for i in range(n):
    res[idx[i]] = dfs(trie,d[idx[i]])
print(1)
print(*res,sep='\n')