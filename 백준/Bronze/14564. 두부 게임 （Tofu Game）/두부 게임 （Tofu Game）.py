n,m,a = map(int,input().split())
ans = []
while True:
    x = int(input())
    if x == m//2+1:
        ans.append(0)
        break
    a = ((a+x-1-(m//2+1))%n+1)
    ans.append(a)
print(*ans,sep='\n')