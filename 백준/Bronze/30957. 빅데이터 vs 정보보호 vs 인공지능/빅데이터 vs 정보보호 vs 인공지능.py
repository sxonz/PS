n = input()
s = input()
B = s.count('B')
S = s.count('S')
A = s.count('A')

m = max(B,S,A)
if B == S == A:
    print('SCU')
else:
    if B == m:
        print('B',end='')
    if S == m:
        print('S',end='')
    if A == m:
        print('A',end='')