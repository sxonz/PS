a,b,c = map(int,input().split())
if b == max(a,c):
    print("Anything")
elif b < max(a,c):
    print("Bus")
else:
    print("Subway")