def solution(n):
    before,current = 0,1
    for i in range(n):
        temp = current
        current += before
        before = temp
    return current % 1234567