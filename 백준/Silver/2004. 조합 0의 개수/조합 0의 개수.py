n,m = map(int,input().split())

def count(n,k):
    res = 0
    while n != 0:
        n //= k
        res += n
    return res

print(min(count(n,5)-count(n-m,5)-count(m,5),count(n,2)-count(n-m,2)-count(m,2)))