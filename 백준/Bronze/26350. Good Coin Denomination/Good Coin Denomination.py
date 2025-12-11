for t in range(int(input())):
    n,*d = list(map(int,input().split()))
    bef = -1
    print("Denominations:",*d)
    for i in d:
        if i < bef*2:
            print("Bad coin denominations!")
            break
        bef = i
    else:
        print("Good coin denominations!")
    print()
            
    