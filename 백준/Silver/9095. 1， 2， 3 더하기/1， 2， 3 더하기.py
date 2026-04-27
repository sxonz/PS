t = int(input())
d = [0,1,2,4]
testcase = []
for test in range(t):
    testcase.append(int(input()))
for i in range(4,max(testcase)+1):
    d.append(d[i-1]+d[i-2]+d[i-3])
for n in testcase:
    print(d[n])