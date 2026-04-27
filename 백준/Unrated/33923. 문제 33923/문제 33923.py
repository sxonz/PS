a,b = map(int,input().split())
if a != b:
    print((min(a,b)-1)**2)
else:
    print((a-2)**2+1)