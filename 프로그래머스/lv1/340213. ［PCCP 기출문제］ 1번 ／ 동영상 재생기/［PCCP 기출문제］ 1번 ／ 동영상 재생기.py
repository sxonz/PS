def prev(t):
    return max(0,t-10)
def next(t,v):
    return min(v,t+10)
def ms_To_s(ms):
    return int(ms[:2]) * 60 + int(ms[3:])
def s_To_ms(s):
    tmp = str(s//60)
    if len(tmp) == 1:
        tmp = "0"+tmp
    tmp2 = str(s%60)
    if len(tmp2) == 1:
        tmp2 = "0"+tmp2
    return tmp + ":" + tmp2
def OpeningProcess(t,s,e):
    return e if s <= t <= e else t
def solution(v, pos, start, end, commands):
    v = ms_To_s(v)
    pos = ms_To_s(pos)
    start = ms_To_s(start)
    end = ms_To_s(end)
    pos = OpeningProcess(pos,start,end)
    for c in commands:
        if c == "prev":
            pos = prev(pos)
        else:
            pos = next(pos,v)
        pos = OpeningProcess(pos,start,end)
    return s_To_ms(pos)