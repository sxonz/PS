def check(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
def solution(numbers, hand):
    answer = []
    pos = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    lp,rp = [3,0],[3,2]
    for i in numbers:
        if i in [1,4,7]:
            roc = 'L'
        elif i in [3,6,9]:
            roc = 'R'
        else:
            print(i,lp,rp,check(lp,pos[i]),check(rp,pos[i]))
            if check(lp,pos[i]) < check(rp,pos[i]):
                roc = 'L'
            elif check(rp,pos[i]) < check(lp,pos[i]):
                roc = 'R'
            else:
                if hand == 'left':
                    roc = 'L'    
                else:
                    roc = 'R'
        answer.append(roc)
        if roc == 'L':lp = pos[i]
        else:rp = pos[i]
    return ''.join(answer)