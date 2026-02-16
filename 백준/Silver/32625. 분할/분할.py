n = int(input())
d = list(map(int,input().split()))

for i in range(1,n):
    if n%i:
        continue
    tmp = set()
    for j in range(0,n,i):
        tmp.add(min(d[j:j+i])+max(d[j:j+i]))
        if len(tmp) > 1:
            break
    else:
        print(1)
        break
else:
    print(0)