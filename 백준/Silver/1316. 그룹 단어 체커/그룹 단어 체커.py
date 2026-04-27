n = int(input())
d = [input() for _ in range(n)]
cnt = 0
for i in d:
    visited = []
    bef = ''
    for j in i:
        if j == bef:
            continue
        if j in visited:
            break
        visited.append(j)
        bef = j
    else:
        cnt += 1
print(cnt)