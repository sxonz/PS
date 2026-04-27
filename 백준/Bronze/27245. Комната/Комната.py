a,b,c = int(input()),int(input()),int(input())
if min(a,b)/c >= 2 and max(a,b)/min(a,b) <= 2:
    print("good")
else:
    print("bad")