testcase = int(input())
d = []
for _ in range(testcase):
    d.append(int(input()))
for idx,val in enumerate(d):
    if val <= 25:
        round = "World Finals"
    elif val <= 1000:
        round = "Round 3"
    elif val <= 4500:
        round = "Round 2"
    else:
        round = "Round 1"
    print("Case #{0}: {1}".format(idx+1,round))