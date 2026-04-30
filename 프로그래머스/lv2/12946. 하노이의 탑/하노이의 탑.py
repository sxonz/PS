def solution(n):
    answer = []
    def hanoi(k,s,e,m):
        if k == 1:
            answer.append([s,e])
            return
        hanoi(k-1,s,m,e)
        answer.append([s,e])
        hanoi(k-1,m,e,s)
    hanoi(n,1,3,2)
    return answer
        
        