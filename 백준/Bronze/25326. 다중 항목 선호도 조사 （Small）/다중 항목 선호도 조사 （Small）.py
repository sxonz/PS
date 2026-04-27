n,m = map(int,input().split())
a = [input().split() for i in range(n)]
for i in range(m):
    s,f,c = input().split()
    tmp = 0
    for j in a:
        if (s == j[0] or s == "-") and (f == j[1] or f == "-") and (c == j[2] or c == "-"):
            tmp += 1
    print(tmp)