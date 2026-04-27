num = list(map(int,input().split()))
min = 99999
for i in range(2):
  for j in range(2):
    if i == 0 and j == 0:min = num[0] if min > num[0] else min
    elif i == 0 and j == 1:min = num[2]-num[0] if min > num[2]-num[0] else min
    elif i == 1 and j == 0: min = num[1] if min > num[1] else min
    elif i == 1 and j == 1: min = num[3]-num[1] if min > num[3]-num[1] else min
print(min)