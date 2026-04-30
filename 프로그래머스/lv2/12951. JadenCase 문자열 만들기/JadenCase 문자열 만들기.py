def solution(s):
    answer = []
    before = ' '
    for i in s.lower():
        if i.isalpha() and before == ' ':
            answer.append(i.upper())
        else:answer.append(i.lower())
        before = i
    return ''.join(answer)
        