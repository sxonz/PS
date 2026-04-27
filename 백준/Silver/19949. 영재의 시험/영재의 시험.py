s=input().replace(' ','')
d,tmp=['1','2','3','4','5'],[]
for i in range(9):
    tmp=[]
    while d:
        a=d.pop()
        for i in range(1,6):
            b=a+str(i)
            if str(i)*3 not in b:
                tmp.append(b)
    d = tmp[::]
res=0
for i in d:
    same=0
    for j in range(10):
        if i[j]==s[j]:
            same+=1
            if same == 5:res += 1;break
print(res)