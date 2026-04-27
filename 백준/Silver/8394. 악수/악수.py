n = int(input())+1
bef,bbef = 1,0
for i in range(2,n):
    bef = (cur := (bbef + (bbef := bef%10))%10)%10
print((bef+bbef)%10)