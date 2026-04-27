n = int(input())
p = list(range(n+1))
def F(x):
    if x-p[x]:p[x] = F(p[x])
    return p[x]
for _ in range(n-2):
    a,b = map(int,input().split())
    a,b = F(a),F(b)
    if a-b:
        if a<b:
            p[b] = a
        else:
            p[a] = b
flag = False
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if F(i)-F(j):
            print(i,j)
            flag = True
            break
    if flag:
        break
