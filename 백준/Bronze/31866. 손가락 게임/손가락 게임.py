a,b = map(int,input().split())
a = 1 if a in [1,3,4] else a
b = 1 if b in [1,3,4] else b
if a == b:
    print('=')
elif a == 1:
    print('<')
elif b == 1:
    print('>')
else:
    if a == 0:
        if b == 2:
            print('>')
        elif b == 5:
            print('<')
    elif a == 2:
        if b == 0:
            print('<')
        elif b == 5:
            print('>')
    else:
        if b == 0:
            print('>')
        else:
            print('<')