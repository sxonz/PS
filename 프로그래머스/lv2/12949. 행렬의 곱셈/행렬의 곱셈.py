def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            temp = 0
            for k,l in zip(arr1[i],arr2):
                temp += k * l[j]
            answer[i][j] = temp
    return answer
            