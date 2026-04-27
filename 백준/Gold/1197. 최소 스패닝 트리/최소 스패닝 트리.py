import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
v,e = map(int, input().split())
edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

parent = [i for i in range(v+1)]

def find(x):
    if parent[x] == x:return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b        

def cycle(a,b):
    return 0 if find(a)-find(b) else 1


answer = 0
for cost,a, b in edges:
    if not cycle(a, b):
        union(a, b)
        answer += cost
print(answer)