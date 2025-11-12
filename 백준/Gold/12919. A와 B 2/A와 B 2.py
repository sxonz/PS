a,b = input(),input()

def find(s):
    if s == a:
        print(1)
        exit()
    if not s:
        return
    if s[-1] == "A":
        find(s[:-1])
    if s[0] == "B":
        find(s[-1:0:-1])
find(b)
print(0)