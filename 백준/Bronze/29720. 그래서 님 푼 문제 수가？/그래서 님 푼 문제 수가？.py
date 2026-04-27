n,m,k = map(int,input().split())
iaxia_ = max(n - (m*k),0)
b = max(n-(m*(k-1))-1,0)
print(iaxia_,b)