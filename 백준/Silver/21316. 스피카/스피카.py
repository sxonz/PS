d = [[] for i in range(13)]
for i in range(12):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
for i in range(1,13):
    if len(d[i]) == 3:
        d[i].sort(key = lambda x:len(d[x]))
        if len(d[d[i][0]]) == 1 and len(d[d[i][1]]) == 2 and len(d[d[i][2]]) == 3:
            print(i)
            