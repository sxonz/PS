def solution(i, j, k):
    return ''.join([str(i) for i in range(i,j+1)]).count(str(k))