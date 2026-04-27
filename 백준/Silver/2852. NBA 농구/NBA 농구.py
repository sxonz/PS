n = int(input())
prev =[0, 0]
team = [0, 0, 0, 0]
for _ in range(n):
    win, time = input().split()
    if win == '1': team[0] += 1
    else: team[2] += 1
    minute, second = map(int, time.split(":"))
    time = minute*60 + second
    if team[0] == team[2]:
        team[3-(prev[1]==1)*2] += time - prev[0]
        prev[1] = 0
    elif team[0] > team[2]:
        if not prev[1]:
            prev = [time,1]
    else:
        if not prev[1]:
            prev = [time,2]

if prev[1] == 1:
    team[1] += 2880 - prev[0]
if prev[1] == 2:
    team[3] += 2880 - prev[0]

print("%02d:%02d" %(team[1]//60, team[1]%60))
print("%02d:%02d" %(team[3]//60, team[3]%60))