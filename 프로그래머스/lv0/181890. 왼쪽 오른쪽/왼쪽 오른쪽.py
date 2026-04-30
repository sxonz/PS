def solution(str_list):
    left = []
    right = []
    s = ""
    for i in str_list:
        if i == 'l' and s != 'r':
            return left
        if s == 'r':
            right.append(i)
        else:
            left.append(i)
        if i == 'r':
            s = 'r'
    return right