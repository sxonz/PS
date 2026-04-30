def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    answer = sum([score[i+m-1] for i in range(0,len(score),m) if i+m <= len(score)])*m  
    return answer
