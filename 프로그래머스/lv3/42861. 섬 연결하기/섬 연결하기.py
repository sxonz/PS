def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    cost = 0
    p = list(range(n))
    def F(x):
        if x != p[x]:p[x] = F(p[x])
        return p[x]
    def U(a,b):
        a,b = F(a),F(b)
        if a<b:
            p[b] = a
        else:
            p[a] = b
    for a,b,c in costs:
        if F(a) != F(b):
            U(a,b)
            cost += c
    return cost