def solution(numbers, direction):
    numbers = [str(i) for i in numbers]
    if direction == 'left':
        return [int(i) for i in numbers[1:] + list(numbers[0])]
    else:
        return [int(i) for i in list(numbers[len(numbers)-1]) + numbers[:len(numbers)-1]]
        