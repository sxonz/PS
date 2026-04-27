n,k=map(int,input().split())
coin=[int(input()) for i in range(n)]
p=n-1
c=0
while k:
    while coin[p] > k:
        p -= 1
    k -= coin[p]
    c += 1
print(c)