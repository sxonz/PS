def solution(dartResult):
    score = [0,0,0]
    mag = {"S":1,"D":2,"T":3}
    before = "31415926535897932384626433832795028"
    test = 0
    num = 0
    for i in dartResult:
        print(num)
        if i.isdigit():
            if not(before.isdigit()) and i.isdigit():
                if before == "*":
                    if num != 0:
                        score[num-1] *= 2
                    score[num] *= 2
                elif before == "#":
                    score[num] *= -1
                num += 1
            if before == "1" and i == "0":
                score[num] += 9
            else:score[num] += int(i)
        elif i in mag.keys():
            score[num] **= mag[i]
        before = i
    if before == "#":
        score[-1] *= -1
    elif before == "*":
        score[-1] *= 2
        score[-2] *= 2
    return sum(score)