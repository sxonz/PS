log = 8
a,b = map(int,input().split())

res = 0
for i in range(a,b+1):
    s = set()
    for j in range(1,log):
        if 10**j > i:
            break
        tmp = str(i%10**j)
        if i%10**j == "0":
            tmp = ''
        r = int(tmp+str(i//10**j))
        if a<=i<r<=b and r not in s:
            res += 1
            s.add(r)
print(res)