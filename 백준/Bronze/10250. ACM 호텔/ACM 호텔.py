for t in range(int(input())):
    h,w,n = map(int,input().split())
    print(((n-1)%h+1)*100+(n-1)//h+1)