d = [[''],['*']]
l = 5

for i in range(2,101):
    temp = []

    temp.append('*'*l)
    temp.append('*'+(' '*(l-2))+'*')
    for j in range(l-4):
        temp.append('*' + ' ' + d[-1][j] + ' ' + '*')
    temp.append('*'+(' '*(l-2))+'*')
    temp.append('*'*l)

    l += 4
    d.append(temp)

for i in d[int(input())]:
    print(i)