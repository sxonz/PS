input()
s = input()
if s.count("A") > s.count("B"):
    print("A")
elif s.count("B") > s.count("A"):
    print("B")
else:
    print("Tie")