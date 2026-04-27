s = input()
idx = 0
r = "UCPC"
for i in s:
    if r[idx] == i:
        idx += 1
        if idx == 4:
            print("I love UCPC")
            break
else:
    print("I hate UCPC")