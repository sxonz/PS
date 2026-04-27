def fact(n):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
    return tmp

n,a,b,c = map(int,input().split())

print(fact(n) // fact(a) // fact(b) // fact(c))