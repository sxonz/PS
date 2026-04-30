def solution(s):
    answer = []
    temp = {}
    for i in s:
        if i not in temp:
            answer.append(-1)
        else:
            answer.append(temp[i])
        temp[i] = 0
        for j in temp.keys():
            temp[j] += 1
    return answer