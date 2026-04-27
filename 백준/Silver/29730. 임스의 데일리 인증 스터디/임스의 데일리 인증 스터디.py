n = int(input())

d = []
boj = []

for _ in range(n):
    temp = input()
    if temp[:7] == 'boj.kr/' and temp != 'boj.kr/':
        boj.append(temp)
    else:
        d.append(temp)
for i in sorted(d,key=lambda x: (len(x),x)):
    print(i)
for i in sorted(boj,key=lambda x:(len(x),x)):
    print(i)