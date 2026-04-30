def solution(before, after):
    return 1 if [1 for i,j in zip(sorted(before),sorted(after)) if i != j] == [] else 0