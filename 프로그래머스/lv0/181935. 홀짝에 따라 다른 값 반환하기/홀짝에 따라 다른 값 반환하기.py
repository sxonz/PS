def solution(n):
    return sum(range(1,n+1,2)) if n % 2 != 0 else sum([i ** 2 for i in range(2,n+1,2)])