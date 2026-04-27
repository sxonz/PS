n = int(input())
bef,cur = 1,1
for i in range(n-2):
    bef,cur = cur,bef+cur
print(cur,n-2)