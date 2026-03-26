d = ["A+","A","B+","B","C+","C","D+","D","F"]
r = [4.5,4,3.5,3,2.5,2,1.5,1,0]
s = input()
cnt = 0
val = 0
for i in range(len(d)):
    cnt += s.count(d[i])
    val += s.count(d[i])*r[i]
    s = s.replace(d[i],'')
print(val/cnt)
