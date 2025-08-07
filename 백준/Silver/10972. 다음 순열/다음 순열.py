n = int(input())
num = list(map(int, input().split()))

flag = True

for i in range(n-1,0,-1):
    if num[i-1] < num[i]:
        for j in range(n-1,0,-1): 
            if num[i-1] < num[j] and flag:
                num[i-1], num[j] = num[j], num[i-1]
                num = num[:i] + sorted(num[i:])
                print(*num)
                flag = False

if flag:
    print(-1)