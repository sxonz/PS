def solution(food):
    food.pop(0)
    food = [(i - i % 2) // 2 for i in food]
    answer = ''
    for i,j in enumerate(food):
        answer += (str(i+1) * j)
    return answer + '0' + ''.join(reversed(list(answer)))
        