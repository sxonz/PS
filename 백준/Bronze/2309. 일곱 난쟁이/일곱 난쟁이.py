d = sorted([int(input()) for _ in range(9)])

flag = False
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        sum = 0
        for k in range(9):
            if k == i or k == j:
                continue
            sum += d[k]
        if sum == 100:
            flag = True
            for k in range(9):
                if k == i or k == j:
                    continue
                print(d[k])
            break
    if flag:
        break