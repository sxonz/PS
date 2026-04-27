s = input()
n = len(s)
cnt = 0
visited = [0]*n
x = 0
while True:
    bef = cnt
    r = "quack"
    idx = 0
    tmp = []
    for i in range(n):
        if not visited[i]:
            if r[idx] == s[i]:
                idx = (idx+1)%5
                tmp.append(i)

    for i in tmp[:len(tmp)-len(tmp)%5]:
        visited[i] = 1
        cnt += 1
    
    if bef==cnt:
        break
    x += 1
if cnt == n:
    print(x)
else:
    print(-1)