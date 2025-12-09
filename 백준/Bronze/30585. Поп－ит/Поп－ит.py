n,m = map(int,input().split())
d = [input() for i in range(n)]
tmp = 0
for i in d:
    tmp += i.count("1")
print(min(tmp,n*m-tmp))