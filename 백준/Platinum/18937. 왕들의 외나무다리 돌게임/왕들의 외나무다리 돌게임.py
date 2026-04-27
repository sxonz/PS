n = int(input())
win = {'Whiteking':'Blackking','Blackking':'Whiteking'}
d = list(map(int,input().split()))
fir = input()
res = 0
for i in d:
    res ^= i-2
if res == 0:
    print(win[fir])
else:
    print(fir)