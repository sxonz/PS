def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = (sum(month[0:a-1]) + b) % 7
    return days[answer]
    