w,h,f,c,x1,y1,x2,y2 = map(int,input().split())
c += 1
m = max(w-f,f)
f = min(w-f,f)

y = y2-y1
l = max(0,f-x1-max(0,f-x2))
r = max(0,x2-x1-l)
print(w*h-(l*y*c*2+r*y*c))