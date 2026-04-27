a,b = map(int,input().split())
a -= a%2^1
b += b%2
print((b-a+1)//2)