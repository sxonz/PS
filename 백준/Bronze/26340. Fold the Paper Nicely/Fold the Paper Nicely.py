for t in range(int(input())):
    a,b,c = map(int,input().split())
    x,y = a,b
    for i in range(c):
        x,y = max(x,y)//2,min(x,y)
    print(f"Data set: {a} {b} {c}")
    print(max(x,y),min(x,y))
    print()