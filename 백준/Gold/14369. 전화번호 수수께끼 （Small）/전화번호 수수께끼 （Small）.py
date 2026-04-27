for t in range(int(input())):
    s = input()
    r = dict()
    for i in s:
        if i not in r:
            r[i] = 0
        r[i] += 1

    ans = []
    for num,i in zip([0,2,4,6,8,1,3,5,7,9],["ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"]):
        flag = True
        while flag:
            for j in i:
                if j not in r or i.count(j) > r[j]:
                    flag = False
                    break
            else:
                ans.append(num)
                for j in i:
                    r[j] -= 1
    s = ''.join([str(i) for i in sorted(ans)])
    print(f"Case #{t+1}: {s}")
