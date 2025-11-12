a,b = input(),input()

def find(s):
    if s == a:
        return 1
    if not s:
        return 0
    r = 0
    if s[-1] == "A":
        r |= find(s[:-1])
    if s[0] == "B":
        r |= find(s[-1:0:-1])
    return r
print(find(b))