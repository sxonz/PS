testcase = int(input())
for i in range(testcase):
    n,s = input().split()
    print(''.join([j*int(n) for j in s]))