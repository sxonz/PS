import re
def solution(skill, skill_trees):
    '''cnt = 0
    for s in skill_trees:
        temp = ''.join([i for i in s if i in skill])
        if re.match(temp,skill[:len(temp)]):
            cnt+=1
    return cnt'''
    return sum([1 for i in skill_trees if re.match(''.join([i for i in s if i in skill]), skill[:len(''.join([i for i in s if i in skill]))])])
            