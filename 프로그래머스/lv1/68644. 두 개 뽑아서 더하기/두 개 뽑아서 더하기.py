def solution(numbers):
    arr = []
    for i in numbers:
        for j in numbers:
            if i == j and numbers.count(i) < 2:
                continue
            arr.append(i+j)
    return sorted(set(arr))