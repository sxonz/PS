try:
    while True:
        a,b,c = map(int,input().split())
        print(max(c-b,b-a)-1)
except:
    pass