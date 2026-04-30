def solution(x, n):
    answer = []
    for i in range(n+1):
        if i == 0:
            continue
        answer.append(i * x)
    return answer