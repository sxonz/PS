def solution(data, ext, val_ext, sort_by):
    q = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    return sorted([i for i in data if i[q[ext]] < val_ext],key = lambda x: x[q[sort_by]])