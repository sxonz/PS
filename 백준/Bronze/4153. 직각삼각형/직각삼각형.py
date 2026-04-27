while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    a,b,c = min(a,b,c),sorted([a,b,c])[1],max(a,b,c)
    ans = 'right' if a*a+b*b == c*c else 'wrong'
    print(ans)