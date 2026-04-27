t = int(input())
testcase = []
for test in range(t):
    testcase.append(int(input()))

zeros = [1,0,1]
ones = [0,1,1]

for i in range(3,max(testcase)+1):
    zeros.append(zeros[i-1]+zeros[i-2])
    ones.append(ones[i-1]+ones[i-2])

for n in testcase:
    print(zeros[n],ones[n])