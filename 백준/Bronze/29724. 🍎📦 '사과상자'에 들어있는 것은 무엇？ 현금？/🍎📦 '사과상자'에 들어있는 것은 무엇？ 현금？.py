e_ = int(input())
g = 0
apples = 0
for _ in range(e_):
    t,w,h,l = input().split()
    if t == "B":
        g += 6000
    else:
        apple = (int(w)//12)*(int(h)//12)*(int(l)//12)
        apples += apple
        g += 500*apple + 1000

print(g)
print(apples*4000)