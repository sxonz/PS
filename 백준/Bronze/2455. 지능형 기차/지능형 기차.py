d = 0
m = 0
for i in range(4):
    a,b = map(int,input().split())
    d = d-a+b
    m = max(d,m)
print(m)