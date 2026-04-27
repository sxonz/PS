import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
d = [i for i in range(n+1)]

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent < b_parent:
        d[b_parent] = a_parent
    else:
        d[a_parent] = b_parent
def find(num):
    if d[num] != num:
        d[num] = find(d[num])
    return d[num]


ans = []
for _ in range(m):
    query,a,b = map(int,input().split())
    if query == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            ans.append('yes')
        else:
            ans.append('no')
for i in ans:
    print(i)