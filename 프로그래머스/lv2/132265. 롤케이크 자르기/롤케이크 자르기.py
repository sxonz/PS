def solution(topping):
    temp,temp2,l,l2,answer,t2 = set(),set(),[],[],[],topping[:]
    topping.reverse()
    for cut in range(len(topping)-1):
        temp.add(t2[cut])
        temp2.add(topping[cut])
        l.append(len(temp))
        l2.append(len(temp2))
    return sum([int(i==j) for i,j in zip(l,reversed(l2))])