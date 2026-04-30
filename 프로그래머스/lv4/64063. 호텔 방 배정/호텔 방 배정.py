def solution(k, room_number):
    answer = []
    visit = {}
    for i in room_number:
        temp=[i]
        while i in visit:
            i = visit[i]
            temp.append(i)
        for j in temp: visit[j] = i + 1
        answer.append(i)
    return answer
                