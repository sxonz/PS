while True:
    n = int(input())
    if not n:
        break
        
    d = [int(input()) for i in range(n)]
    d.sort()
    d += [(1422-d[-1])*2+d[-1]]
    if any([d[i+1]-d[i]>200 for i in range(n)]):
        print("IM",end='')
    print("POSSIBLE")