a = 'G...'
b = '.I.T'
c = '..S.'

d = ''
e = ''
f = ''

n = int(input())

for i in a:
    d += i*n
for i in b:
    e += i*n
for i in c:
    f += i*n
for i in range(n):
    print(d)
for i in range(n):
    print(e)
for i in range(n):
    print(f)