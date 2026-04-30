from itertools import permutations
def solution(age):
    d = list(permutations(["문","성","중","학","교"],2))
    print(d)
    print(len(d))
