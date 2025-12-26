def dist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2
for t in range(int(input())):
    d = [tuple(map(int,input().split())) for i in range(4)]
    flag = False
    for i in {0,1,2,3}:
        for j in {0,1,2,3}-{i}:
            for k in {0,1,2,3}-{i,j}:
                l = 6-i-j-k
                if dist(*d[i],*d[j]) == dist(*d[j],*d[k]) == dist(*d[k],*d[l]) == dist(*d[l],*d[i]) and dist(*d[i],*d[k]) == dist(*d[j],*d[l]):
                    flag = True
    print(flag*1)