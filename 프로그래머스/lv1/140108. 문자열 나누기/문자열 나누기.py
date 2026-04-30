def solution(s):
    ycnt = 0
    ncnt = 0
    first = ''
    brk = True
    answer = 0
    for i in s:
        if brk == True:
            first = i
        if first == i:
            ycnt += 1
        else:
            ncnt += 1
        if ycnt == ncnt:
            answer += 1
            ycnt,ncnt = 0,0
            brk = True
        else:
            brk = False
        print(ycnt,ncnt)
    if ycnt != 0 or ncnt != 0:
        answer += 1
    return answer
            
        
        
        