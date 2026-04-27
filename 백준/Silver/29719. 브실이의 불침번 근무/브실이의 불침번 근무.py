def power(a, n):
    if n == 0:
        return 1
    
    x = power(a, n//2)

    if n % 2 == 0:
        return x * x
    
    else:
        return x * x * a

n,m = map(int,input().split())

print((power(m,n)-power(m-1,n)) % 1000000007)