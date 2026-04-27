n,k = map(int,input().split())
tmp = 1
while k:
    if tmp-1==n:
        print(0)
        break
    if n % tmp == 0:
        k -= 1
    tmp += 1
else:
    print(tmp-1)
    