def solution(name, yearning, photo):
    answer = []
    for i in photo:
        temp = 0
        for j,k in enumerate(name):
            temp += i.count(k) * yearning[j]
        answer.append(temp)
    return answer
    