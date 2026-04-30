def solution(sides):
    return len(range(abs(sides[0]-sides[1])-1, sum(sides)))