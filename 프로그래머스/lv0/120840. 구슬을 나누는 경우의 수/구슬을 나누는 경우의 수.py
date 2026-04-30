from math import factorial
def solution(n, m):
    return factorial(n) // (factorial(n-m)*factorial(m))