def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer: answer.append(i)
    for j in range(k-len(answer)):
        answer.append(-1)
    return answer[:k]