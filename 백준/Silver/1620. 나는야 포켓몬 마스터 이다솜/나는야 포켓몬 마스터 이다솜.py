n,m = map(int,input().split())
d = [input() for i in range(n)]
idx = {i:j for i,j in zip(d,range(1,n+1))}
for i in range(m):
    s = input()
    if s.isdigit():
        print(d[int(s)-1])
    else:
        print(idx[s])