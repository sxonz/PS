import sys
input = lambda:sys.stdin.readline().rstrip()
n = 0
dic = dict()
while 1:
    word = input()
    if not word:
        break
    n += 1   
    if word not in dic:
        dic[word] = 0
    dic[word] += 1
sdic = dict(sorted(dic.items()))
for i in sdic:
    a = sdic[i]
    print(i,"%.4f" %((a / n  * 100)))