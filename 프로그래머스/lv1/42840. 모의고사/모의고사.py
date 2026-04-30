def solution(answers):
    score = [0,0,0]
    mans = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i,j in enumerate(answers):
        for k in range(3):
            if mans[k][i % len(mans[k])] == j:
                score[k] += 1
    answer = []
    for i,j in enumerate(score):
        if j == max(score):
            answer.append(i+1)
    return answer
            