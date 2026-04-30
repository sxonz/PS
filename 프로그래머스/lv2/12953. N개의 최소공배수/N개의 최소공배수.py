def solution(arr):
    sum = 1
    for i in arr:
        sum *= i
    for i in range(sum):
        if i == 0:
            continue
        b = True
        for j in arr:
            if i % j != 0:
                b = False
        if b == True:
            return i
    return sum