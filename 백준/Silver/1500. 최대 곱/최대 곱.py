s, k = map(int,input().split())
print((t:=s//k)**(k-s%k) * (t+1)**(s%k))
