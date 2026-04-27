n = int(input())
d = sorted([int(input()) for _ in range(n)])

def c(lst):
    cnt = 0
    for i in lst:
        if i != 0:
            cnt += 1
    return cnt


res = 0
for i in range(n):
    check = [0]*n
    check[i] = 1

    for j in range(i+1,n):
        for k in range(i,j):
            if d[k] + check[k] >= d[j]:
                check[j] = check[k] + 1
                break
        else:
            break
    
    for j in range(i-1,-1,-1):
        for k in range(i,j,-1):
            if d[k] - check[k] <= d[j]:
                check[j] = check[k] + 1
                break
        else:
            break
    
    res = max(res,c(check))
print(res)