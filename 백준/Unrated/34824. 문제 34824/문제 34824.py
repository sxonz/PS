n = int(input())
d = [input() for i in range(n)]
if d.index("yonsei") < d.index("korea"):
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")