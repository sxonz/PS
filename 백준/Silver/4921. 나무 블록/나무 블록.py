bef = {1:[],2:[4,6],3:[4,6],4:[1,3],5:[1,3],6:[8],7:[8],8:[5,7]}
t = 0
while True:
    t += 1
    r = list(map(int,input()))
    if r == [0]:
        break
    flag = True
    if r[0] != 1 or r[-1] != 2:
        flag = False
    for i in range(1,len(r)):
        if r[i-1] not in bef[r[i]]:
            flag = False
        if not flag:
            break
    print(f"{t}. {["NOT","VALID"][flag]}")