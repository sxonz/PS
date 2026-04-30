def solution(citations):
    return max(map(min,enumerate(sorted(citations,reverse=True),start=1)))