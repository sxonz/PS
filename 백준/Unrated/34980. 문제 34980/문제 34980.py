n = int(input())
s,t = input(),input()
a = s.count("w")
b = t.count("w")
if a>b:
    print("Oryang")
elif a<b:
    print("Manners maketh man")
elif a == b:
    if s!=t:
        print("Its fine")
    else:
        print("Good")