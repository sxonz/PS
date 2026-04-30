def solution(cards1, cards2, goal):
    g=[]
    for i in goal:
        if len(cards1) != 0:
            if cards1[0] == i:
                g.append(cards1.pop(0))
                continue
        if len(cards2) != 0:
            if cards2[0] == i:
                g.append(cards2.pop(0))
    
    return 'Yes' if goal == g else 'No'