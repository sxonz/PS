a,b = map(int,input().split())
m = 10**7+2
check = [False]*m
prime = []
for i in range(2,m):
    if not check[i]:
        if i**2 > b:
            break
        prime.append(i)
        k = 2
        while i*k < m:
            check[i*k] = True
            k += 1
cnt = 0
for i in prime:
    cur = i*i
    while cur <= b:
        if cur >= a:
            cnt += 1
        cur *= i
print(cnt)
    

    
    

    
    
