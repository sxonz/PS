def solution(n):
    n2 = str(n)
    answer = 0
    for i in range(len(n2)):
        answer += int(n2[i])

    return answer