def solution(array):
    d = {}
    for i in array:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    key = []
    value = []
    for i in d:
        key.append(i)
        value.append(d[i])
    return -1 if value.count(max(value)) >= 2 else key[value.index(max(value))]
        
    