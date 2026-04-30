def solution(X, Y):
    Xn = {}
    Yn = {}
    n = []
    for i in X:
        if i not in Xn:
            Xn[i] = 1
        else:Xn[i] += 1
    for i in Y:
        if i not in Yn:
            Yn[i] = 1
        else:Yn[i] += 1
    i = 0
    while i < 10:
        if str(i) in Xn and str(i) in Yn:
            if Xn[str(i)] >= 1 and Yn[str(i)] >= 1:
                n.append(str(i))
                Xn[str(i)] -= 1
                Yn[str(i)] -= 1
        if str(i) not in Xn or str(i) not in Yn:
            i += 1
        else:
            if Xn[str(i)] < 1 or Yn[str(i)] < 1:
                i += 1
    n = ''.join(sorted(n,reverse=True))
    if not(n):return "-1"
    return "0" if n[0] == "0" else n