n = int(input())
s = input()
if "R" not in s or "B" not in s:
    print(0)
    exit()
print(min(s[s.find("R"):].count("B"),s[s.find("B"):].count("R"),s[:s.rfind("R")].count("B"),s[:s.rfind("B")].count("R")))