h,n = map(int,input().split())
d = [tuple([*map(int,input().split()),i]) for i in range(n)]
d.sort(key=lambda x:x[1])
res = dict()
for i in range(n):
    res[d[i][2]] = i+1

print("YES")
for i in range(n):
    print(res[i],end=' ')