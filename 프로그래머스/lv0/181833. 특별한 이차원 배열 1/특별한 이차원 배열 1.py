def solution(n):
    answer = []
    for i in range(n):
        sum = []
        for j in range(n):
            if i == j:
                sum.append(1)
            else:
                sum.append(0)
        answer.append(sum)
    return answer
            