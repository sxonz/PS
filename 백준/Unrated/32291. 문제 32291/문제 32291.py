n = int(input())+1
ans = set([1])
for i in range(2,int(n**0.5+1)):
    if n%i == 0:
        if n//i > (n-1)//i:
            ans.add(i)
            ans.add(n//i)
ans = list(ans)
ans.sort()
print(*ans)
