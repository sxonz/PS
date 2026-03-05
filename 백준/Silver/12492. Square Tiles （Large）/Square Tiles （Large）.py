for t in range(int(input())):
    n,m = map(int,input().split())
    d = [input() for i in range(n)]
    r = 0
    for i in d:
        r += i.count("#")
    res = [['.' for i in range(m)] for j in range(n)]
    cnt = 0
    for i in range(n-1):
        for j in range(m-1):
            if res[i][j] != ".":
                continue
            if d[i][j] == "#" and d[i+1][j] == "#" and d[i][j+1] == "#" and d[i+1][j+1] == "#":
                cnt += 4
                res[i][j] = "/"
                res[i+1][j] = "\\"
                res[i][j+1] = "\\"
                res[i+1][j+1] = "/"
    print(f"Case #{t+1}:")
    if cnt == r:
        for i in res:
            print(''.join(i))
    else:
        print("Impossible")

                