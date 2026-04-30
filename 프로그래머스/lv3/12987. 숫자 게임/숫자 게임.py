def solution(A, B):
    A.sort()
    B.sort()
    cnt,indexa,indexb,l = 0,0,0,len(A)
    while True:
        if A[indexa] < B[indexb]:
            cnt += 1
            indexa += 1
            indexb += 1
        else:
            indexb += 1
        if indexb >= l:
            break
    return cnt
        