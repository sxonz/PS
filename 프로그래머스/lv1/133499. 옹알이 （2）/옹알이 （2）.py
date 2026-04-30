def solution(babbling):
    count = 0
    for i in babbling:
        if 'aya' in i:
            if 'ayaaya' not in i:
                i = i.replace('aya',' ')
            else:
                continue
        if 'ye' in i:
            if 'yeye' not in i:
                i = i.replace('ye',' ')
            else:
                continue
        if 'woo' in i:
            if 'woowoo' not in i:
                i = i.replace('woo',' ')
            else:
                continue
        if 'ma' in i:
            if 'mama' not in i:
                i = i.replace('ma',' ')
        if i.replace(' ','') == '':
            count += 1
    return count
            