n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
idx = {j:i for i,j in enumerate(a)}
d = [idx[i]+1 for i in b]
bstree = [0]*(n+1)

def search(x):
    res = 0
    while x:
        res += bstree[x]
        x -= x&-x
    return res

def update(x):
    while x <= n:
        bstree[x] += 1
        x += x&-x

r = 0
for i in range(n):
    r += i-search(d[i])
    update(d[i])
print(r)
