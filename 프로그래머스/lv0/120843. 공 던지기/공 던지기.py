def solution(numbers, k):
    numbers *= k
    return numbers[(k-1) * 2]