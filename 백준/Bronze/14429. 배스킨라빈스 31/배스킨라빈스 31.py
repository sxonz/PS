game = int(input())
res,l=  [],0
for i in range(game):
    n,m = map(int,input().split())
    r = (n-1)%(m+1)
    res.append(((n-1-r)//(m+1)*2)+2)
print(res.index(min(res))+1,min(res))