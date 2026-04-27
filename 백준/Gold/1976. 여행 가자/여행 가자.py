n = int(input())
m = int(input())
d = [i for i in range(n)]

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

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if i == j:
            continue
        if tmp[j] == 1:
            union(i,j)
trip = list(map(int,input().split()))
t = find(trip[0]-1)
for i in range(m):
    if trip[i] > n:
        print('NO')
        break
    if t != find(trip[i]-1):
        print('NO')
        break
else:
    print('YES')