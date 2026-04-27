cnt = [6,2,5,5,4,5,6,3,7,6]

MAX = 100
n = int(input())
for i in range(MAX):
    for j in range(MAX):
        r = i+j
        if r>=MAX:
            continue
        tmp = cnt[i//10]+cnt[i%10]+cnt[j//10]+cnt[j%10]+cnt[r//10]+cnt[r%10]+4
        if tmp == n:
            i = str(i)
            i = (2-len(i))*"0"+i
            j = str(j)
            j = (2-len(j))*"0"+j
            r = str(r)
            r = (2-len(r))*"0"+r
            print(f"{i}+{j}={r}")
            exit()
print("impossible")