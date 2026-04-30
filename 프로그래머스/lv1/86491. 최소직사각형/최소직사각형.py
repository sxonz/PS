def solution(sizes):
    bigger = []
    smaller = []
    for i in sizes:
        i = sorted(i)
        smaller.append(i[0])
        bigger.append(i[1])
    return max(bigger) * max(smaller)
    