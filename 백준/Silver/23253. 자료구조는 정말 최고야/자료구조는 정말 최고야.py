n,m = map(int,input().split())
flag = False
for i in range(m):
    k = int(input())
    d = list(map(int,input().split()))
    bef = int(1e9)
    for j in d:
        if j > bef:
            flag = True
            break
        bef = j

    if flag:
        break
print("YNeos"[flag::2])
