dp = [1]
bef = cur = 1
for i in range(479):
    dp.append(cur := bef + (bef := cur))
while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print(sum([1 for i in dp if a<=i<=b]))