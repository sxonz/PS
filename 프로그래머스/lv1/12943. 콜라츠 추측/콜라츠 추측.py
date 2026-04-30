def solution(num):
    if num == 1:return 0
    for i in range(1,502):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i
    return -1
    