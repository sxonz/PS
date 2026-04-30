def solution(s):
    s = list(s)
    middle = len(s) / 2 if len(s) % 2 == 0 else len(s) // 2
    middle = int(middle)
    return s[middle] if len(s) % 2 != 0 else s[middle-1] + s[middle]