def solution(N, number):
    cases = [set() for i in range(1,10)]
    for i in range(1,9):
        case = cases[i]
        case.add(int(str(N)*i))
        for j in range(1,i):
            for k in cases[j]:
                for l in cases[i-j]:
                    case.add(k+l)
                    case.add(k-l)
                    case.add(k*l)
                    if 0 not in [k,l]:case.add(k//l)
        if number in case:
            return i
    return -1