def solution(k, score):
    temp = []
    answer = []
    for i,j in enumerate(score):
        temp.append(j)
        temp.sort(reverse=True)
        if len(temp) > k:
            temp.pop(k)
        if len(temp) < k:
            answer.append(temp[-1])
        else:
            answer.append(temp[k-1])
    return answer