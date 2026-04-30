import re
import itertools
def solution(user_id, banned_id):
    temp = len(banned_id)
    temp2 = []
    answer = []
    
    banned_id = ' '.join(banned_id).replace('*','.')
    for i in itertools.permutations(user_id,temp):
        sum = ' '.join(i)
        if re.fullmatch(banned_id,sum):
            temp2.append(sorted(list(i)))
    for i in temp2:
        if i not in answer:
            answer.append(i)
    return len(answer)