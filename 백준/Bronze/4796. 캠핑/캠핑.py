i = 1
while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (0,0,0):
        break
    print(f"Case {i}: {c//b*a+min(c%b,a)}")
    i += 1