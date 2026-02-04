h,m = 0,0
d = [(0,0)]
for i in range(360):
    h += 1
    m = (m+12)%360
    d.append((h,m))
a,b = map(int,input().split())
print("XO"[(a,b) in d])