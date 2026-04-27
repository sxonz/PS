for t in range(int(input())):
    n,r = map(int,input().split())
    print("YNeos"[r-n!=10000000::2])