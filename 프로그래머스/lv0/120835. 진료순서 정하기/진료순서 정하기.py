def solution(emergency):
    temp = sorted(emergency,reverse=True)
    return [temp.index(i) + 1 for i in emergency]