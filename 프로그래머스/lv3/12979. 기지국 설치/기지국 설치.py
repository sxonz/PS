def solution(n, stations, w):
    cur = 0
    res = 0
    size = w*2+1
    for i in stations+[n+w+1]:
        res += (i-w-cur-1)//size + ((i-w-cur-1)%size != 0)
        cur = i+w
    return res