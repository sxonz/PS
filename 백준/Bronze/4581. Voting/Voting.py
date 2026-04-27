while True:
    s = input()
    if s == '#':
        break
    if s.count('A') >= len(s) / 2:
        print('need quorum')
        continue
    if s.count('Y') > s.count('N'):
        print('yes')
    elif s.count('N') > s.count('Y'):
        print('no')
    else:
        print('tie')