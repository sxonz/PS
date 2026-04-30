def solution(n, w, num):
    d1 = (w - (num-1)%w - 1)*2 + 1
    d2 = w*2 - d1
    
    box = 0
    while True:
        num += d1
        if num>n:
            break
        box += 1
        num += d2
        if num>n:
            break
        box += 1
    return box+1