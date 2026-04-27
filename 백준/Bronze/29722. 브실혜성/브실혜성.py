y,m,d = map(int,input().split("-"))
num = int(input())
d += num

n,d = divmod(d,30)
m += n

n,m = divmod(m,12)
y += n

if d <= 0:
    d += 30
    m -= 1
if m <= 0:
    m += 12
    y -= 1
if d < 10:
    d = "0"+str(d)
if m < 10:
    m = "0"+str(m)
print("{0}-{1}-{2}".format(y,m,d))