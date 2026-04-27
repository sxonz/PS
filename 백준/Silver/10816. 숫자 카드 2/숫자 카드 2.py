n = int(input())
nums = sorted(list(map(int,input().split())))
m = int(input())
f = list(map(int,input().split()))

temp = {}
for i in nums:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
for i in f:
    if i not in temp:
        print(0,end=" ")
        continue
    print(temp[i],end=" ")