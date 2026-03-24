a,b = map(int,input().split(":"))
def gcd(x,y):
    return x if not y else gcd(y,x%y)
print(f"{a//gcd(a,b)}:{b//gcd(a,b)}")