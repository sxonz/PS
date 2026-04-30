def solution(array, commands):
    answer = []
    for i,j in enumerate(commands):
        sum = array[j[0]-1:j[1]]
        sum.sort()
        answer.append(sum[j[2]-1])
    return answer
        