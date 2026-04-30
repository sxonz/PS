def solution(arr):
    sum = 0
    for i in arr:
        if i == 2:
            break
        sum += 1
    for i in range(sum):
        arr.pop(0)
    arr.reverse()
    sum = 0
    for i in arr:
        if i == 2:
            break
        sum += 1
    for i in range(sum):
        arr.pop(0)
    arr.reverse()
    return arr if arr else [-1]