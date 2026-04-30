def solution(clothes):
    array=dict()
    for i in clothes:
        if i[1] in array:
            array[i[1]].append(i[0])
        else:
            array.setdefault(i[1],[i[0]])
    sum=[]
    for i in array.values():
        sum.append(len(i)+1)
    s = 1
    for i in sum:
        s *= i
    return s - 1