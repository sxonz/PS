def solution(numbers):
    notinnumbers = [i for i in range(10) if i not in numbers]
    return sum(notinnumbers)