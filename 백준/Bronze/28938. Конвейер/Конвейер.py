input()
r = sum(map(int,input().split()))
if r>0:
    print("Right")
elif r==0:
    print("Stay")
else:
    print("Left")