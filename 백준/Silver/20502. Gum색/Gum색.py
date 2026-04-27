n,m = map(int,input().split())
d = list(map(int,input().split()))
k = {i : [] for i in range(1,m+1)}

for i in range(n):
    c,*r = map(int,input().split())
    for j in r:
        k[j].append(i+1)
for i in k:
    if k[i]:
        k[i] = sorted(k[i], key = lambda x:d[x-1])
    else:
        k[i] = [-1]
q = int(input())
for query in range(q):
    print(*k[int(input())])
    