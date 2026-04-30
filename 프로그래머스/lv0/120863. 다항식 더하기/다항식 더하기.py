def solution(polynomial):
    answer = [0,0]
    for i in polynomial.split(" "):
        if i == '+':
            continue
        elif i == 'x':
            answer[0] += 1
        elif i[-1] == 'x':
            answer[0] += int(i[:len(i)-1])
        else:
            answer[1] += int(i)
    if answer[0] == 0:
        return str(answer[1])
    if answer[0] == 1:
        if answer[1] == 0:
            return 'x'
        return ''.join(['x ','+ ',str(answer[1])]) if answer[1] >= 1 else ''.join([str(answer[0]),'x'])
    return ''.join([str(answer[0]),'x ','+ ',str(answer[1])]) if answer[1] >= 1 else ''.join([str(answer[0]),'x'])
        