n = int(input())
dice = list(map(int,input().split()))
reward = [0,0,0,0,0]
def get(s):
    if 35<=s<65:return 0
    if 65<=s<95:return 1
    if 95<=s<125:return 2
    if 125<=s:return 3
    return 4
time = 0
tinc = 4
sinc = 1
curs = 0
for d in dice:
    if time > 240:
        reward[get(curs)] += 1
        time = 0;tinc = 4;sinc = 1;curs = 0
    if d == 1:
        reward[get(curs)] += 1
        time = 0;tinc = 4;sinc = 1;curs = 0
        continue
    if d == 2:
        if sinc > 1: sinc //= 2
        else: tinc += 2
    if d == 4: time += 56
    if d == 5 and tinc > 1:
        tinc -= 1
    if d == 6 and sinc<32:sinc *= 2
    time += tinc; curs += sinc
for i in reward[:4]:
    print(i)