from itertools import permutations
def solution(numbers):
    return max([i[0]*i[1] for i in permutations(numbers,2)])