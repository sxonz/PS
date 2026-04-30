def solution(n, m, section):
    count = 0
    while len(section) > 0:
        current = section[0] + m
        while len(section) != 0 and current > section[0]:
            section.pop(0)
        count += 1
    return count