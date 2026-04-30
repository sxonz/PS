def solution(sides):
    return 1 if sides.pop(sides.index(max(sides))) < sum(sides) else 2