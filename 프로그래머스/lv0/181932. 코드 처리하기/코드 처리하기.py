def solution(code):
    ret = []
    mode = 0
    for idx,val in enumerate(code):
        if val == '1':
            mode = mode * (-1) + 1
        elif mode == 0 and idx % 2 == 0:
            ret.append(val)
        elif mode == 1 and idx % 2 == 1:
            ret.append(val)

    return ''.join(ret) if ret else "EMPTY"
    