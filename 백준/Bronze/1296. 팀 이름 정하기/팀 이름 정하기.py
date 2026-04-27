key = input()
d = [input() for i in range(int(input()))]
r = []
cnt = [key.count("L"),key.count("O"),key.count("V"),key.count("E")]
for i in d:
    tmp = [cnt[0]+i.count("L"),cnt[1]+i.count("O"),cnt[2]+i.count("V"),cnt[3]+i.count("E")]
    val = ((tmp[0]+tmp[1])*(tmp[0]+tmp[2])*(tmp[0]+tmp[3])*(tmp[1]+tmp[2])*(tmp[1]+tmp[3])*(tmp[2]+tmp[3]))%100
    r.append((-val,i))
r.sort()
print(r[0][1])