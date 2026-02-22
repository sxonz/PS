while True:
    d = list(map(int,input().split()))
    if not sum(d):
        break
    d.sort()
    if d[2] >= d[0]+d[1]:
        print("Invalid")
    elif d[0] == d[2]:
        print("Equilateral")
    elif d[0] == d[1] or d[1] == d[2]:
        print("Isosceles")
    else:
        print("Scalene")