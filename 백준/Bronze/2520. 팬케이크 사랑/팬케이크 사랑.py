for t in range(int(input())):
    input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dough = min(a[0]/8,a[1]/8,a[2]/4,a[3],a[4]/9)*16//1
    print(int(min(dough,b[0]+b[1]//30+b[2]//25+b[3]//10)))