def solution(bandage, health, attacks):
    r = 0
    t,x,y = bandage
    current = health
    for i in range(1,attacks[-1][0]+1):
        if attacks[0][0] == i:
            r = 0
            current -= attacks[0][1]
            if current <= 0:
                current = -1
                break
            attacks.pop(0)
        else:
            r += 1
            if r == t:
                current = min(current+y,health)
                r = 0
            current = min(current+x,health)
    return current
            