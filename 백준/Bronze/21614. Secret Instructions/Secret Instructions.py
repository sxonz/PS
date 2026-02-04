bef = 0
r = {1:"left",0:"right"}
while True:
    s = input()
    if s == "99999":
        break
    tmp = int(s[0])+int(s[1])
    if tmp==0:
        print(r[bef],s[2:])
    elif tmp%2:
        print("left",s[2:])
        bef = 1
    else:
        print("right",s[2:])
        bef = 0