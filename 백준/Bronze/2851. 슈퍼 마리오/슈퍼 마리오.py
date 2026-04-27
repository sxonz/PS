d = [int(input()) for _ in range(10)]
print(sorted([sum(d[:i+1]) for i in range(10)],key=lambda x:(abs(100-x),-x))[0])