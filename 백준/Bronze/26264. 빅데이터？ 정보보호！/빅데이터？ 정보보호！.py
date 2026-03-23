n = int(input())
s = input()
big,sec = s.count("bigdata"),s.count("security")
if big>sec:
    print("bigdata?")
elif sec>big:
    print("security!")
else:
    print("bigdata? security!")
