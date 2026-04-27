def time(word):
    dial,t = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO',7: 'PQRS', 8: 'TUV', 9: 'WXYZ'},0
    for c in word:
        for n,l in dial.items():
            if c in l:
                t += n+1
                break 
    return t
print(time(input()))
