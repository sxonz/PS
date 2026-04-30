def check(i):
    while i % 2 == 0:
        i //= 2
    if i == 1:
        return False
    return True
def solution(arr):
    while check(len(arr)):
        arr.append(0)
    return arr