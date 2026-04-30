from collections import deque
def check(arr):
    temp = []
    for i in arr:
        if i in ["(","{","["]:
            temp.append(i)
        else:
            if i == ")" and "(" in temp:
                temp.pop(temp.index("("))
            elif i == "}" and "{" in temp:
                temp.pop(temp.index("{"))
            elif i == "]" and "[" in temp:
                temp.pop(temp.index("["))
            else:
                return 0
    return 1 if len(temp)==0 else 0
def solution(s):
    if len([1 for i in ["(",")","{","}","[","]"] if s.count(i) == 0]) != 0:return 0
    s = deque(s)
    temp = s
    answer = 0
    for idx in range(len(s)):
        temp.rotate(-1)
        if check(list(temp)) == 1:
            answer += 1
    return answer