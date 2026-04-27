ans = []
for i in range(5):
    if "FBI" in input():
        ans.append(i+1)
if ans:
    print(*ans)
else:
    print("HE GOT AWAY!")