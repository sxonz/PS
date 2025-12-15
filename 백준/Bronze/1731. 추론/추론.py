n = int(input())
d = [int(input()) for i in range(n)]
a,b = d[1]-d[0],d[1]//d[0]
bef = d[0]
af,bf = 1,1
for i in d[1:]:
    if bef+a != i:
        af = 0
    if bef*b != i:
        bf = 0
    bef = i
if af:
    print(d[-1]+a)
elif bf:
    print(d[-1]*b)