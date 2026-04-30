def solution(k, tangerine):
    answer = 0
    temp = {}
    for i in tangerine:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    arr = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    if arr[0][1] >= k:
        return 1
    else:
        sum = 0
        for i,j in arr:
            if sum < k:
                sum += j
                answer += 1
            else:
                return answer
