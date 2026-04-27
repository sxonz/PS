a,b = map(int,input().split(":"))
s,e = map(int,input().split(":"))
a %= 12
s %= 12
x = a*60+b
y = s*60+e
print(min(abs(x-y)*6,4320-abs(y-x)*6))