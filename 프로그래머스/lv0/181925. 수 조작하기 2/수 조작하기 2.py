def solution(numLog):
    math = { 1:'w',-1:'s',10:'d',-10:'a'}
    answer = []
    for i in range(1,len(numLog)):
        answer.append(math[numLog[i]-numLog[i-1]])
    return ''.join(answer)
        