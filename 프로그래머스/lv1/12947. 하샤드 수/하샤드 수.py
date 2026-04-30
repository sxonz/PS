def solution(x):
    sumx = 0
    strx = str(x)
    for i in range(len(strx)):
        indexx = strx[i]
        sumx += int(indexx)
    print(sumx)
    print(x)
    return True if x % sumx == 0 else False