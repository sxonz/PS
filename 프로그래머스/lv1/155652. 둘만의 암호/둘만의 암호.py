import string
def solution(s, skip, index):
    
    str = list(string.ascii_lowercase)
    for i in skip:str.pop(str.index(i))
    str *= 5
    
    answer = ''
    for i in s:
        answer += str[str.index(i)+index]
    return answer
            
        