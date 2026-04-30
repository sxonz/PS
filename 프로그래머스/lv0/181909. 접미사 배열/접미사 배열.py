def solution(s):
    return sorted([s[len(s)-i-1:] for i in range(len(s))])