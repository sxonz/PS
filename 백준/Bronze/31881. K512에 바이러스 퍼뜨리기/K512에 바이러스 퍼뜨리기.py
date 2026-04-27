import sys
input = sys.stdin.readline

n,q = map(int,input().split())
d = {}
d[0] = False
for i in range(1,n+1):
    d[i] = True

cur = n
res = []

for _ in range(q):
    query = input()
    if query[0] == '3':
        res.append(cur)
    else:
        query,num = map(int,query.split())
        if query == 1:
            if d[num]:
                cur -= 1
                d[num] = False
        else:
            if not d[num]:
                cur += 1
                d[num] = True

for i in res:
    print(i)