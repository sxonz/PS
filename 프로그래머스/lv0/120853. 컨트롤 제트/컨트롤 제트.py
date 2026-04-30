def solution(s):
    answer = 0
    before = 0
    for i in s.split(' '):
        if i == 'Z':
            answer -= before
        else:
            answer += int(i)
            before = int(i)
    return answer