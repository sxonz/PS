s = int(input())
n = list(map(int,input().split()))
m = max(n)
temp = []
for i in n:
    temp.append(i / m * 100)
print(sum(temp)/s)