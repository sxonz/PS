def solution(score):
    score = list(map(lambda x:(x[0]+x[1])/2,score))
    sor = sorted(score,reverse=True)
    ans = []
    for i in score:
        ans.append(sor.index(i)+1)
    return ans