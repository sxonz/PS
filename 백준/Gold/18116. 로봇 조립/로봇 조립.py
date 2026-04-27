import sys
input = sys.stdin.readline
n = int(input())
p = dict()
c = dict()
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
for _ in range(n):
    q = input().split()
    if q[0] == "I":
        a,b = int(q[1]),int(q[2])
        if a not in c:
            c[a] = 1
            p[a] = a
        if b not in c:
            c[b] = 1
            p[b] = b
        a,b = F(a),F(b)
        if a!=b:
            if a<b:
                c[a] += c[b]
                p[b] = a
            else:
                c[b] += c[a]
                p[a] = b
    else:
        a = int(q[1])
        if a not in p:
            print(1)
        else:
            print(c[F(a)])
        