n = int(input())
d = list(map(int,input().split()))
y,m = 0,0
for i in d:
    i+=1
    y += i // 30 * 10
    if i % 30:
        y += 10
    m += i // 60 * 15
    if i % 60:
        m += 15

if y>m:
    print("M",m)
elif m>y:
    print("Y",y)
else:
    print("Y M",y)