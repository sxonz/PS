def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        sum = []
        for j in range(n):
            sum.append(num_list[i+j])
        answer.append(sum)
    return answer