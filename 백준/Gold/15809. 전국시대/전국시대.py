n,m = map(int,input().split())
army = [0] + [int(input()) for _ in range(n)]
parents = [-i for i in army]
def Find(x):
    if parents[x] < 0: return x
    parents[x] = Find(parents[x])
    return parents[x]
def W_Union(a,b):
    a,b = Find(a),Find(b)
    if a == b:
        parents[a] = -1
        parents[b] = -1
    elif parents[a] < parents[b]:
        parents[a] -= parents[b]
        parents[b] = a
    else:
        parents[b] -= parents[a]
        parents[a] = b
def A_Union(a,b):
    a,b = Find(a),Find(b)
    if a < b:
        parents[a] += parents[b]
        parents[b] = a
    else:
        parents[b] += parents[a]
        parents[a] = b
for i in range(m):
    query,a,b = map(int,input().split())
    if query == 1:
        A_Union(a,b)
    else:
        W_Union(a,b)
parents = [-i for i in parents if i < 0]
print(len(parents))
if parents:
    parents.sort()
    print(*parents)