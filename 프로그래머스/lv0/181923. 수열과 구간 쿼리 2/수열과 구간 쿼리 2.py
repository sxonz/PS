def solution(arr, queries):
    answer = []
    for query in queries:
        s,e,k = query
        temp = []
        for i in range(s,e+1):
            if arr[i] > k:
                temp.append(arr[i])
        if temp: answer.append(min(temp))
        else:answer.append(-1)
    return answer
        