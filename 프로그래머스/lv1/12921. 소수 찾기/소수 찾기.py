def solution(n):
    temp = set(range(3,n+1,2))
    for i in range(3,n+1,2):
        if i in temp:
            temp -= set(range(i*2,n+1,i))
    return len(temp) + 1
    
        
        