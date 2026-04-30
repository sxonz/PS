def solution(A,B):
    A = sorted(A)
    B = sorted(B,reverse=True)
    answer = 0
    for i,j in zip(A,B):
        answer += i*j
    return answer