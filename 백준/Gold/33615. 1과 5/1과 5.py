testcase = int(input())
for test in range(testcase):
    n = input()
    if set(n) == set("5"):
        print(0,5)
        continue
    if set(n) == set("1") and len(n) > 3:
        print(len(n)%2,11)
        continue
    mod = 0
    for i in n:
        mod += int(i)
    mod %= 3
    if mod == 0:
        print(0,3)
    elif mod == 1:
        print(n.find("1")+1,3)
    else:
        print(n.find("5")+1,3)
