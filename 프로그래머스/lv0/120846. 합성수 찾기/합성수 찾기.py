def check(n):
    for i in range(2,n):
        if n % i == 0:
            return True
    return False
def solution(n):
    return sum([1 for i in range(1,n+1) if check(i)])