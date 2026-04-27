n = int(input())
d = list(map(int,input().split()))
for i in range(2,1000001):
    if i in d:
        continue
    for j in d:
        if i // j not in d:
            break
        if i % j != 0:
            break
    else:
        print(i)
        break