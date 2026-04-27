import sys
input = sys.stdin.readline
testcase = int(input())
for ts in range(testcase):
    n = int(input())
    p = dict()
    def F(x):
        if str(p[x]).isdigit():return x
        p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[a] += p[b]
            p[b] = a
        else:
            p[b] += p[a]
            p[a] = b
    for i in range(n):
        a,b = input().split()
        if a not in p:
            p[a] = 1
        if b not in p:
            p[b] = 1
        if F(a) != F(b):
            U(a,b)
        print(p[F(a)])
    