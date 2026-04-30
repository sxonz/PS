def solution(spell, dic):
    dic = list(map(sorted,dic))
    spell = str(sorted(spell))
    for t in dic:
        if str(t) == spell:
            return 1
    return 2