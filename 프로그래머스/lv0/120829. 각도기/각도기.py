def solution(angle):
    if angle < 90:
        return 1
    return 3 if angle % 90 != 0 else angle // 90 * 2