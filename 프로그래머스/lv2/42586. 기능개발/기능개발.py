def solution(progresses, speeds):
    days = 0
    bapo = []
    while progresses:
        for i,j in enumerate(progresses):
            progresses[i]  = j + speeds[i]
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count >= 1:
            bapo.append(count)
                
    return bapo